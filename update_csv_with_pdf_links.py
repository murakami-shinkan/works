import csv
import os
import re
import unicodedata

def normalize_string(s):
    """
    比較のために文字列を正規化する。
    - 全角文字を半角に変換する。
    - 様々な記号やスペースを置換する。
    - 小文字に変換する。
    """
    # ステップ1: NFKC正規化（全角を半角に変換など）
    s = unicodedata.normalize('NFKC', s)

    # ステップ2: ファイル名によくあるプレフィックスを削除
    # 例: "著者名[年号] - タイトル" から "タイトル" の部分を抽出
    s = re.sub(r'^.*?\[\d{4}[a-z]?\]\s*-\s*', '', s)

    # ステップ3: 記号をスペースに置換
    replacements = {
        '—': ' ', '―': ' ', '‐': ' ', '-': ' ', '−': ' ', '–': ' ',
        '~': ' ', '～': ' ', '(': ' ', ')': ' ', '「': ' ', '」': ' ',
        '『': ' ', '』': ' ', '【': ' ', '】': ' ', ':': ' ', '：': ' ',
        ',': ' ', '、': ' ', '。': ' ', '.': ' ', '?': ' ', '!': ' ',
        '*': ' ', '#': ' '
    }
    for old, new in replacements.items():
        s = s.replace(old, new)

    # ステップ4: 連続する空白を一つにまとめ、小文字に変換
    s = ' '.join(s.split()).strip()
    return s.lower()

def find_matching_pdf(title, pdf_files_map):
    """タイトルに一致するPDFファイルを探す"""
    normalized_title = normalize_string(title)
    return pdf_files_map.get(normalized_title)

def main():
    """
    CSVファイルのF列をPDFファイルへの相対パスで更新する
    """
    csv_file_path = 'data/master-2.csv'
    output_csv_path = 'data/master-2_updated.csv'
    pdf_dir = 'PDF'
    
    if not os.path.isdir(pdf_dir):
        print(f"エラー: ディレクトリ '{pdf_dir}' が見つかりません。")
        return
    
    try:
        pdf_files = [f for f in os.listdir(pdf_dir) if f.lower().endswith('.pdf')]
        if not pdf_files:
            print(f"警告: '{pdf_dir}' 内にPDFファイルが見つかりません。")
            return
    except OSError as e:
        print(f"エラー: ディレクトリ '{pdf_dir}' の読み込み中にエラーが発生しました: {e}")
        return
    
    # パフォーマンス向上のため、正規化済みのPDFファイル名を辞書にキャッシュする
    pdf_files_map = {
        normalize_string(os.path.splitext(f)[0]): f 
        for f in pdf_files
    }
    
    try:
        with open(csv_file_path, 'r', newline='', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            rows = list(reader)
    except FileNotFoundError:
        print(f"エラー: ファイル '{csv_file_path}' が見つかりません。")
        return
    except Exception as e:
        print(f"エラー: ファイル '{csv_file_path}' の読み込み中にエラーが発生しました: {e}")
        return
    
    if not rows:
        print("CSVファイルが空です。")
        return
    
    header = rows[0]
    try:
        title_col_index = header.index('Title')
        pdf_link_col_index = header.index('PDF_Link')
    except ValueError as e:
        print(f"エラー: CSVヘッダーに必要な列が見つかりません: {e}")
        return
    
    updated_count = 0
    unmatched_titles = []
    for i, row in enumerate(rows[1:], start=1):
        if len(row) <= title_col_index or not row[title_col_index]:
            continue
        
        title = row[title_col_index]
        matching_pdf_filename = find_matching_pdf(title, pdf_files_map)
        
        if matching_pdf_filename:
            relative_path = os.path.join(pdf_dir, matching_pdf_filename).replace(os.sep, '/')
            if len(row) > pdf_link_col_index and not row[pdf_link_col_index]:
                row[pdf_link_col_index] = relative_path
                updated_count += 1
                print(f"✅ Match Found (Row {i+1}):")
                print(f"  - Title: '{title}'")
                print(f"  - PDF  : '{relative_path}'")
        else:
            unmatched_titles.append(f"行 {i+1}: {title}")
    
    try:
        with open(output_csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
    except Exception as e:
        print(f"エラー: ファイル '{output_csv_path}' への書き込み中にエラーが発生しました: {e}")
        return
    
    print(f"\n処理が完了しました。")
    print(f"{updated_count}件のPDFリンクを更新し、結果を '{output_csv_path}' に保存しました。")
    
    if unmatched_titles:
        print("\n--- 一致するPDFが見つからなかったタイトル ---")
        for unmatched in unmatched_titles[:20]:
            print(unmatched)

if __name__ == '__main__':
    main()
