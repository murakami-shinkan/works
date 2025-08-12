## 新SSOTマスターデータスキーマ解説表

| 列名 | 説明 | 入力例 |
| :--- | :--- | :--- |
| **ProjectID** | プロジェクト内で各業績に付与する一意の識別子 | `msk0770` |
| **GyosekiNo** | 著作目録PDF 上の番号一次情報源とのトレーサビリティを確保 | `論文-75` |
| **DataSource** | このデータの主たる典拠`GyosekiPDF`, `INBUDS`, `GitHubPDF`, `LegacyWorksheet`など | `GyosekiPDF` |
| **Status** | 各データの作業進捗`1_New`, `2_Consolidated`, `3_Reconciled`, `4_Verified`など | `1_New` |
| **ReconciliationNotes** | データソース間の齟齬と、それに対する判断を記録する | `著作目録とINBUDSでページ数が1頁異なる著作目録の197頁を正とする` |
| **GitHub\\_PDF\\_Link** | GitHubリポジトリ内の対応するPDFへの直接リンク | `https://github.com/murakami-shinkan/works/blob/main/paper-075.pdf` |
| **INBUDS\\_ArticleID** | INBUDSに収録済みの場合、その論文識別コード | `0-001234-5678` |
| **INBUDS\\_MediaID** | INBUDSに収録済みの場合、その媒体識別コード | `1234-5678` |
| **ArticleType** | INBUDSの論文種別コード1:論文, 2:論文翻訳, 6:書評など | `1` |
| **Language** | INBUDSの使用言語コード1:日本語, 2:英語, 7:サンスクリット語など | `2` |
| **AuthorshipType** | INBUDSの執筆区分コード1:著, 2:共著, 5:編など | `1` |
| **Author\\_FamilyName** | 筆者の姓（漢字） | `村上` |
| **Author\\_FirstName** | 筆者の名（漢字） | `真完` |
| **Author\\_FamilyName\\_Roman** | 筆者の姓（ローマ字） | `Murakami` |
| **Author\\_FirstName\\_Roman** | 筆者の名（ローマ字） | `Shinkan` |
| **Author\\_FamilyName\\_Yomi** | 筆者の姓（よみ・カタカナ） | `ムラカミ` |
| **Author\\_FirstName\\_Yomi** | 筆者の名（よみ・カタカナ） | `シンカン` |
| **Author\\_Affiliation** | 執筆当時の所属・肩書 | `東北大学文学部` |
| **Title** | 論文の主たる論題 | `Purusa of the Samkhya Philosophy and atman of the Vedānta Philosophy` |
| **Title\\_Yomi** | 論題のよみ（カタカナ） | `プルシャ オブ ザ サーンクヤ フィロソフィー アンド アートマン オブ ザ ヴェーダーンタ フィロソフィー` |
| **Subtitle** | 論文の副題 | `with reference to the so-called Pañcaśikha Fragment 4` |
| **Title\\_JA\\_Translation** | 欧文論題の和訳 | `サーンクヤ哲学のプルシャとヴェーダーンタ哲学のアートマン` |
| **Title\\_EN\\_Translation** | 和文論題の英訳 | `On the Four Brahma-vihāras in the Āgamas` |
| **Subtitle\\_JA\\_Translation** | 欧文副題の和訳 | `いわゆるパンチャシカ断片4に関連して` |
| **Subtitle\\_EN\\_Translation** | 和文副題の英訳 | `Focusing on the Self-Island and Self-Reliance` |
| **PageStart** | 掲載開始ページ | `169` |
| **PageEnd** | 掲載終了ページ | `197` |
| **PageWritingDirection** | ページ進行方向のコード1:横書, 2:縦書 | `1` |
| **Publication\\_MediaName** | 掲載媒体（雑誌・書籍）名 | `Journal of the Oriental Institute, M. S. University of Baroda` |
| **Publication\\_MediaName\\_Yomi** | 媒体名のよみ（カタカナ） | `ジャーナル オブ ジ オリエンタル インスティテュート エム エス ユニバーシティ オブ バローダ` |
| **Publication\\_MediaName\\_EN** | 媒体名の欧文表記 | `Journal of the Oriental Institute, M. S. University of Baroda` |
| **Publication\\_PartName** | 部編名（例：上巻、思想編など） | `(空欄)` |
| **Publication\\_Theme** | 特集・テーマ名 | `佐藤博士古稀記念` |
| **Publication\\_Editor** | 編著者名 | `雲井昭善` |
| **Publisher** | 発行者・発行所 | `M. S. University of Baroda` |
| **Publication\\_Country** | 発行国コード1:日本, 2:その他 | `2` |
| **Publication\\_Place** | 発行地 | `Baroda` |
| **Publication\\_Date** | 発行年月日（西暦 YYYY-MM-DD形式） | `1980-06-30` |
| **Volume** | 巻 | `XXIX` |
| **Issue** | 号 | `3-4` |
| **SerialNumber** | 通号 | `170` |
| **ISSN** | 国際標準逐次刊行物番号 | `0030-5324` |
| **ISBN** | 国際標準図書番号 | `978-4393111277` |
| **Keyword\\_Region** | キーワード：地域 | `インド` |
| **Keyword\\_Period** | キーワード：時代 | `古代` |
| **Keyword\\_Field** | キーワード：分野 | `インド哲学` |
| **Keyword\\_Person** | キーワード：人物 | `Pañcaśikha` |
| **Keyword\\_Document** | キーワード：文献 | `Sāṃkhyakārikā` |
| **Keyword\\_Term** | キーワード：術語 | `puruṣa` |"
