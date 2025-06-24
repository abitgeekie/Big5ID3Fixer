# Big5 ID3 Fixer
Big5ID3Fixer is a Python program to fix the Chinese encoding issue for ID3 attributes for MP3 files. This provides an easy-to-use solution for updating the metadata of songs in a folder.

這是一個用來解決在Unicode普及之前(如Windows 95時代)所產生的 MP3 檔案中 ID3 標籤，在現代Unicode系統裡以亂碼呈現的問題。這 Python 程式提供了一個可行的解決方案，用於更新資料夾內歌曲的中繼資料。

---
### Features (特點)
Automatic detection of legacy Chinese encoding in ID3 tags
Conversion of incorrectly encoded ID3 tags to properly encoded Unicode
Support for batch processing of music files
Compatible with both ID3v1 and ID3v2 tags

自動偵測 ID3 標籤中老舊的中文編碼
將錯誤編碼的 ID3 標籤轉換為正確的 Unicode
支援音樂檔案的批次處理
相容於 ID3v1 和 ID3v2 標籤

### Installation (安裝)
This assumes you already have Python 3 installed.
(This is tested on Windows 11. )

You have installed the mutagen library first.
（已在 Windows 11 上測試確認。）
你必須先安裝 mutagen。
