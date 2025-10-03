## 新SSOTマスターデータスキーマ解説表

|列| 列名 | 説明 | 入力例 |
| :---| :--- | :--- | :--- |
|A| **ProjectID** | プロジェクト内で各業績に付与する一意の識別子 | `msk0770` |
|B| **GyosekiNo** | 著作目録PDF 上の番号一次情報源とのトレーサビリティを確保 | `論文-75` |
|C| **DataSource** | このデータの主たる典拠`GyosekiPDF`, `INBUDS`, `GitHubPDF`, `LegacyWorksheet`など | `GyosekiPDF` |
|D| **Status** | 各データの作業進捗`1_New`, `2_Consolidated`, `3_Reconciled`, `4_Verified`など | `1_New` |
|E| **ReconciliationNotes** | データソース間の齟齬と、それに対する判断を記録する | `著作目録とINBUDSでページ数が1頁異なる著作目録の197頁を正とする` |
|F| **GitHub_PDF_Link** | GitHubリポジトリ内の対応するPDFへの直接リンク | `https://github.com/murakami-shinkan/works/blob/main/paper-075.pdf` |
|G| **INBUDS_ArticleID** | INBUDSに収録済みの場合、その論文識別コード | `0-001234-5678` |
|H| **INBUDS_MediaID** | INBUDSに収録済みの場合、その媒体識別コード | `1234-5678` |
|I| **ArticleType** | INBUDS執筆区分コード１: 論文, ２: 論文翻訳, ３: 原典校訂, ４: 原典翻訳, ５: 目録・索引, ６: 書評, ７: 報告, ８: 対談・シンポジウム・座談会, ９: 講演, 10: 伝記・死亡記事, 11: その他 | `1` |
|J| **Language** | INBUDS使用言語コード１: 日本語, ２: 英語, ３:フランス語, ４: ドイツ語, ５: 中国語, ６: 韓国語, ７: サンスクリット語, ８: チベット語, ９: 漢文, 10: その他| `2` |
|K| **AuthorshipType** | INBUDS執筆区分コード１: 著, ２: 共著, ３: 訳, ４: 共訳, ５: 編, ６: 共編,　7: 監修| `1` |
|L| **Author_FamilyName** | 筆者の姓（漢字） | `村上` |
|M| **Author_FirstName** | 筆者の名（漢字） | `真完` |
|N| **Author_FamilyName_Roman** | 筆者の姓（ローマ字） | `Murakami` |
|O| **Author_FirstName_Roman** | 筆者の名（ローマ字） | `Shinkan` |
|P| **Author_FamilyName_Yomi** | 筆者の姓（よみ・カタカナ） | `ムラカミ` |
|Q| **Author_FirstName_Yomi** | 筆者の名（よみ・カタカナ） | `シンカン` |
|R| **Author_Affiliation** | 執筆当時の所属・肩書 | `東北大学文学部` |
|S| **Title** | 論文の主たる論題 | `Purusa of the Samkhya Philosophy and atman of the Vedānta Philosophy` |
|T| **Title_Yomi** | 論題のよみ（カタカナ） | `プルシャ オブ ザ サーンクヤ フィロソフィー アンド アートマン オブ ザ ヴェーダーンタ フィロソフィー` |
|U| **Subtitle** | 論文の副題 | `with reference to the so-called Pañcaśikha Fragment 4` |
|V| **Title_JA_Translation** | 欧文論題の和訳 | `サーンクヤ哲学のプルシャとヴェーダーンタ哲学のアートマン` |
|W| **Title_EN_Translation** | 和文論題の英訳 | `On the Four Brahma-vihāras in the Āgamas` |
|X| **Subtitle_JA_Translation** | 欧文副題の和訳 | `いわゆるパンチャシカ断片4に関連して` |
|Y| **Subtitle_EN_Translation** | 和文副題の英訳 | `Focusing on the Self-Island and Self-Reliance` |
|Z| **PageStart** | 掲載開始ページ | `169` |
|AA| **PageEnd** | 掲載終了ページ | `197` |
|AB| **PageWritingDirection** | ページ進行方向のコード1:横書, 2:縦書 | `1` |
|AC| **Publication_MediaName** | 掲載媒体（雑誌・書籍）名 | `Journal of the Oriental Institute, M. S. University of Baroda` |
|AD| **Publication_MediaName_Yomi** | 媒体名のよみ（カタカナ） | `ジャーナル オブ ジ オリエンタル インスティテュート エム エス ユニバーシティ オブ バローダ` |
|AE| **Publication_MediaName_EN** | 媒体名の欧文表記 | `Journal of the Oriental Institute, M. S. University of Baroda` |
|AF| **Publication_PartName** | 部編名（例：上巻、思想編など） | `(空欄)` |
|AG| **Publication_Theme** | 特集・テーマ名 | `佐藤博士古稀記念` |
|AH| **Publication_Editor** | 編著者名 | `雲井昭善` |
|AI| **Publisher** | 発行者・発行所 | `M. S. University of Baroda` |
|AJ| **Publication_Country** | 発行国コード1:日本, 2:その他 | `2` |
|AK| **Publication_Place** | 発行地 | `Baroda` |
|AL| **Publication_Date** | 発行年月日（西暦 YYYY-MM-DD形式） | `1980-06-30` |
|AM| **Volume** | 巻 | `XXIX` |
|AN| **Issue** | 号 | `3-4` |
|AO| **SerialNumber** | 通号 | `170` |
|AP| **ISSN** | 国際標準逐次刊行物番号 | `0030-5324` |
|AQ| **ISBN** | 国際標準図書番号 | `978-4393111277` |
|AR| **Keyword_Region** | キーワード：地域 | `インド` |
|AS| **Keyword_Period** | キーワード：時代 | `古代` |
|AT| **Keyword_Field** | キーワード：分野 | `インド哲学` |
|AU| **Keyword_Person** | キーワード：人物 | `Pañcaśikha` |
|AV| **Keyword_Document** | キーワード：文献 | `Sāṃkhyakārikā` |
|AW| **Keyword_Term** | キーワード：術語 | `puruṣa` |"
