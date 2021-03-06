二选一

【Django】
1. 请参照所提供截图data_model.png，用python3新建一个Django项目，自定义models.py，并生成数据库中的Book表。
2. 简单起见，数据库可以选用SQLite。如果使用PostgreSQL或者MySQL，也欢迎尝试。
3. 使用loaddata往数据库中导入至少50万条数据，可随机自动生成。
4. 基于Django框架，实现基本的增删查改REST接口。要求能用浏览器REST client类插件跑通。
5. 重点考察翻页功能，例如每页10条数据，翻到第1000页。每页20条数据，翻到第500页。
6. 请于收到题目24小时内提交整个项目，并附上操作说明。

【统一数据访问】
1. 请参照所提供截图data_model.png，新建一个后端项目，实现统一的数据访问。
2. 数据存储要求选用传统RDBMS（如SQLite、PostgreSQL或者MySQL等）和大数据相关平台（如HDFS、HBase、Hive、MongoDB等）各一种。
3. 往数据源中导入至少50万条数据，可随机自动生成。
4. 实现统一的增删查改REST接口，不同的数据源设定为参数。要求能用浏览器REST client类插件跑通。
5. 重点考察查询与下载功能，例如下载位于多个数据源的某作者的全部书籍，保存为csv文件。
6. 请于收到题目72小时内提交整个项目，并附上操作说明。