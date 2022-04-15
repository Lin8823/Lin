### Files 

1.[land_crawler](https://github.com/Lin8823/Lin/blob/main/%E4%B8%80%E9%A8%B0%E8%B3%87%E8%A8%8A/land_crawler.py) --內政部不動產時價登錄網 爬蟲程式  

2.[land_data](https://github.com/Lin8823/Lin/tree/main/%E4%B8%80%E9%A8%B0%E8%B3%87%E8%A8%8A/land_data) --臺北市/新北市/桃園市/臺中市/高雄市 108年第2季不動產買賣資料

3.[land_pyspark](https://github.com/Lin8823/Lin/blob/main/%E4%B8%80%E9%A8%B0%E8%B3%87%E8%A8%8A/land_pyspark.py) --pySpark篩選資料集

4.[result-part1.json](https://github.com/Lin8823/Lin/blob/main/%E4%B8%80%E9%A8%B0%E8%B3%87%E8%A8%8A/result-part1.json) -- filter output to json  

* 【主要用途】為【住家用】  
* 【建物型態】為【住宅大樓】  
* 【總樓層數】需【大於等於十三層】

5.[land](https://github.com/Lin8823/Lin/tree/main/%E4%B8%80%E9%A8%B0%E8%B3%87%E8%A8%8A/land) --Flask API
* 將land資料夾下載後，至終端機將工作路徑轉至land資料夾，並使用 ```falsk run``` 指令，啟動flask專案



**Reference:**  
* PySpark  
  * [不負責任教學- Pyspark](http://davidhnotes.com/pyspark-intro2/)
  * [(PySpark版)如何完成從頭到尾完成一個資料科學專案](https://medium.com/jackys-blog/pyspark%E7%89%88-%E5%A6%82%E4%BD%95%E5%AE%8C%E6%88%90%E5%BE%9E%E9%A0%AD%E5%88%B0%E5%B0%BE%E5%AE%8C%E6%88%90%E4%B8%80%E5%80%8B%E8%B3%87%E6%96%99%E7%A7%91%E5%AD%B8%E5%B0%88%E6%A1%88-dbf0a6ec9f59)
  * [Spark RDD (Resilient Distributed Datasets) 詳細圖文介紹](https://yjhyjhyjh0.pixnet.net/blog/post/411468760) 
* [python map](https://www.wongwonggoods.com/python/python-map/)
