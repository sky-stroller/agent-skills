# SQLite DB Ops (SQLite 数据库操作)

## 概述

SQLite DB Ops 是一个完整的 SQLite 数据库操作技能，提供全面的增删改查 (CRUD) 功能。通过简单的命令行接口或 Python API，你可以轻松管理 SQLite 数据库，无需编写重复的数据库操作代码。

## 适用场景

此技能适用于以下场景：

- 创建或管理 SQLite 数据库
- 执行数据库的增删改查操作
- 批量数据导入导出
- 执行自定义 SQL 查询
- 查看数据库结构和表信息
- 快速原型开发和数据分析
- 数据库迁移和备份

## 核心工具

### db_operations.py - 数据库操作脚本

**位置**: [`skills/sqlite-db-ops/scripts/db_operations.py`](../skills/sqlite-db-ops/scripts/db_operations.py)

**功能**: 提供完整的 SQLite CRUD 操作，支持命令行和 Python API 两种使用方式

**支持的操作**:
- `create_table` - 创建数据库表
- `insert` - 插入单条或批量数据
- `query` - 查询数据（支持条件、排序、限制）
- `update` - 更新数据
- `delete` - 删除数据
- `execute` - 执行自定义 SQL 语句
- `list_tables` - 列出所有表
- `table_info` - 查看表结构

## 使用方法

### 命令行使用

#### 1. 创建表

```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py <数据库路径> create_table \
  --table <表名> \
  --columns '<列定义JSON>'
```

**示例**:
```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db create_table \
  --table users \
  --columns '{"id": "INTEGER PRIMARY KEY AUTOINCREMENT", "name": "TEXT NOT NULL", "email": "TEXT", "age": "INTEGER"}'
```

**列定义格式**: JSON 对象，键为列名，值为 SQLite 类型和约束

#### 2. 插入数据

**插入单条数据**:
```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py <数据库路径> insert \
  --table <表名> \
  --data '<数据JSON>'
```

**示例**:
```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db insert \
  --table users \
  --data '{"name": "张三", "email": "zhangsan@example.com", "age": 25}'
```

**批量插入**:
```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db insert \
  --table users \
  --data '[
    {"name": "李四", "email": "lisi@example.com", "age": 30},
    {"name": "王五", "email": "wangwu@example.com", "age": 28}
  ]'
```

**数据格式**: JSON 对象（单条）或 JSON 数组（批量）

#### 3. 查询数据

```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py <数据库路径> query \
  --table <表名> \
  [--columns <列名>] \
  [--where <WHERE子句>] \
  [--params <参数JSON数组>] \
  [--order-by <排序字段>] \
  [--limit <限制数量>]
```

**示例**:

查询所有数据:
```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db query --table users
```

条件查询（使用参数化查询防止 SQL 注入）:
```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db query \
  --table users \
  --where 'age > ?' \
  --params '[25]'
```

指定列和排序:
```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db query \
  --table users \
  --columns 'name, email' \
  --order-by 'age DESC' \
  --limit 10
```

复杂条件:
```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db query \
  --table users \
  --where 'age > ? AND name LIKE ?' \
  --params '[20, "%张%"]'
```

#### 4. 更新数据

```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py <数据库路径> update \
  --table <表名> \
  --data '<更新数据JSON>' \
  --where <WHERE子句> \
  [--params <参数JSON数组>]
```

**示例**:
```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db update \
  --table users \
  --data '{"age": 26}' \
  --where 'name = ?' \
  --params '["张三"]'
```

更新多个字段:
```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db update \
  --table users \
  --data '{"age": 26, "email": "newemail@example.com"}' \
  --where 'id = ?' \
  --params '[1]'
```

#### 5. 删除数据

```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py <数据库路径> delete \
  --table <表名> \
  --where <WHERE子句> \
  [--params <参数JSON数组>]
```

**示例**:
```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db delete \
  --table users \
  --where 'age < ?' \
  --params '[20]'
```

删除特定记录:
```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db delete \
  --table users \
  --where 'id = ?' \
  --params '[5]'
```

#### 6. 执行自定义 SQL

```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py <数据库路径> execute \
  --sql '<SQL语句>' \
  [--params <参数JSON数组>]
```

**示例**:

聚合查询:
```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db execute \
  --sql 'SELECT name, COUNT(*) as count FROM users GROUP BY name'
```

联表查询:
```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db execute \
  --sql 'SELECT u.name, o.total FROM users u JOIN orders o ON u.id = o.user_id WHERE o.total > ?' \
  --params '[100]'
```

#### 7. 查看数据库信息

**列出所有表**:
```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db list_tables
```

**查看表结构**:
```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db table_info --table users
```

输出示例:
```json
[
  {
    "cid": 0,
    "name": "id",
    "type": "INTEGER",
    "notnull": 0,
    "dflt_value": null,
    "pk": 1
  },
  {
    "cid": 1,
    "name": "name",
    "type": "TEXT",
    "notnull": 1,
    "dflt_value": null,
    "pk": 0
  }
]
```

#### 8. 输出到文件

所有查询操作都支持 `--output` 参数将结果保存为 JSON 文件：

```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db query \
  --table users \
  --output results.json
```

### Python API 使用

脚本可以作为 Python 模块导入使用：

```python
from scripts.db_operations import SQLiteDB

# 使用上下文管理器（推荐）
with SQLiteDB('data.db') as db:
    # 创建表
    db.create_table('users', {
        'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'name': 'TEXT NOT NULL',
        'email': 'TEXT',
        'age': 'INTEGER'
    })
    
    # 插入单条数据
    user_id = db.insert('users', {
        'name': '张三',
        'email': 'zhangsan@example.com',
        'age': 25
    })
    
    # 批量插入
    db.insert_many('users', [
        {'name': '李四', 'email': 'lisi@example.com', 'age': 30},
        {'name': '王五', 'email': 'wangwu@example.com', 'age': 28}
    ])
    
    # 查询数据
    results = db.query('users', where='age > ?', params=(20,))
    for user in results:
        print(f"{user['name']}: {user['age']}")
    
    # 更新数据
    db.update('users', {'age': 26}, where='name = ?', params=('张三',))
    
    # 删除数据
    db.delete('users', where='id = ?', params=(1,))
    
    # 执行自定义 SQL
    stats = db.execute_sql('SELECT AVG(age) as avg_age FROM users')
    print(f"平均年龄: {stats[0]['avg_age']}")
```

手动管理连接:
```python
db = SQLiteDB('data.db')
db.connect()

try:
    # 执行操作
    results = db.query('users')
finally:
    db.close()
```

## SQLite 数据类型

| 类型 | 说明 | 示例 |
|------|------|------|
| `INTEGER` | 整数 | 1, 42, -100 |
| `REAL` | 浮点数 | 3.14, -0.5 |
| `TEXT` | 文本字符串 | "Hello", "张三" |
| `BLOB` | 二进制数据 | 图片、文件 |
| `NULL` | 空值 | NULL |

## 常用约束

| 约束 | 说明 | 示例 |
|------|------|------|
| `PRIMARY KEY` | 主键，唯一标识 | `id INTEGER PRIMARY KEY` |
| `AUTOINCREMENT` | 自动递增 | `id INTEGER PRIMARY KEY AUTOINCREMENT` |
| `NOT NULL` | 非空 | `name TEXT NOT NULL` |
| `UNIQUE` | 唯一值 | `email TEXT UNIQUE` |
| `DEFAULT <值>` | 默认值 | `status TEXT DEFAULT 'active'` |
| `CHECK (<条件>)` | 检查约束 | `age INTEGER CHECK(age >= 0)` |
| `FOREIGN KEY` | 外键 | `FOREIGN KEY(user_id) REFERENCES users(id)` |

## 完整工作流程示例

### 示例 1: 用户管理系统

```bash
# 1. 创建用户表
python3 skills/sqlite-db-ops/scripts/db_operations.py users.db create_table \
  --table users \
  --columns '{
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "username": "TEXT UNIQUE NOT NULL",
    "email": "TEXT NOT NULL",
    "created_at": "TEXT DEFAULT CURRENT_TIMESTAMP"
  }'

# 2. 插入管理员用户
python3 skills/sqlite-db-ops/scripts/db_operations.py users.db insert \
  --table users \
  --data '{"username": "admin", "email": "admin@example.com"}'

# 3. 批量导入用户
python3 skills/sqlite-db-ops/scripts/db_operations.py users.db insert \
  --table users \
  --data '[
    {"username": "user1", "email": "user1@example.com"},
    {"username": "user2", "email": "user2@example.com"}
  ]'

# 4. 查询所有用户
python3 skills/sqlite-db-ops/scripts/db_operations.py users.db query --table users

# 5. 更新用户邮箱
python3 skills/sqlite-db-ops/scripts/db_operations.py users.db update \
  --table users \
  --data '{"email": "newemail@example.com"}' \
  --where 'username = ?' \
  --params '["admin"]'

# 6. 查看表结构
python3 skills/sqlite-db-ops/scripts/db_operations.py users.db table_info --table users
```

### 示例 2: 销售数据分析

```bash
# 1. 创建销售表
python3 skills/sqlite-db-ops/scripts/db_operations.py sales.db create_table \
  --table sales \
  --columns '{
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "product": "TEXT",
    "amount": "REAL",
    "quantity": "INTEGER",
    "date": "TEXT"
  }'

# 2. 批量导入销售数据
python3 skills/sqlite-db-ops/scripts/db_operations.py sales.db insert \
  --table sales \
  --data '[
    {"product": "产品A", "amount": 1500.50, "quantity": 10, "date": "2024-01-01"},
    {"product": "产品B", "amount": 2300.00, "quantity": 15, "date": "2024-01-02"},
    {"product": "产品A", "amount": 1800.00, "quantity": 12, "date": "2024-01-03"}
  ]'

# 3. 按产品聚合统计
python3 skills/sqlite-db-ops/scripts/db_operations.py sales.db execute \
  --sql 'SELECT product, SUM(amount) as total, SUM(quantity) as qty, COUNT(*) as orders FROM sales GROUP BY product'

# 4. 查询高额订单
python3 skills/sqlite-db-ops/scripts/db_operations.py sales.db query \
  --table sales \
  --where 'amount > ?' \
  --params '[2000]' \
  --order-by 'amount DESC'

# 5. 导出报表
python3 skills/sqlite-db-ops/scripts/db_operations.py sales.db query \
  --table sales \
  --order-by 'date DESC' \
  --output sales_report.json
```

### 示例 3: 任务管理应用

```bash
# 1. 创建任务表
python3 skills/sqlite-db-ops/scripts/db_operations.py tasks.db create_table \
  --table tasks \
  --columns '{
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "title": "TEXT NOT NULL",
    "description": "TEXT",
    "status": "TEXT DEFAULT \"pending\"",
    "priority": "INTEGER DEFAULT 0",
    "created_at": "TEXT DEFAULT CURRENT_TIMESTAMP"
  }'

# 2. 添加任务
python3 skills/sqlite-db-ops/scripts/db_operations.py tasks.db insert \
  --table tasks \
  --data '{"title": "完成项目文档", "description": "编写README和API文档", "priority": 1}'

# 3. 查询待办任务
python3 skills/sqlite-db-ops/scripts/db_operations.py tasks.db query \
  --table tasks \
  --where 'status = ?' \
  --params '["pending"]' \
  --order-by 'priority DESC, created_at ASC'

# 4. 标记任务完成
python3 skills/sqlite-db-ops/scripts/db_operations.py tasks.db update \
  --table tasks \
  --data '{"status": "completed"}' \
  --where 'id = ?' \
  --params '[1]'

# 5. 删除旧任务
python3 skills/sqlite-db-ops/scripts/db_operations.py tasks.db delete \
  --table tasks \
  --where 'status = ? AND created_at < ?' \
  --params '["completed", "2024-01-01"]'
```

## 最佳实践

### 1. 使用参数化查询

**✅ 正确**:
```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db query \
  --table users \
  --where 'name = ?' \
  --params '["张三"]'
```

**❌ 错误** (容易 SQL 注入):
```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db query \
  --table users \
  --where "name = '张三'"
```

### 2. 备份数据库

在执行批量更新或删除前：
```bash
cp data.db data.db.backup
```

### 3. 验证操作结果

插入后查询验证：
```bash
# 插入数据
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db insert \
  --table users \
  --data '{"name": "测试用户", "email": "test@example.com"}'

# 验证插入
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db query \
  --table users \
  --where 'email = ?' \
  --params '["test@example.com"]'
```

### 4. 使用事务

批量操作自动在一个事务中完成：
```bash
# 批量插入会在单个事务中执行
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db insert \
  --table users \
  --data '[/* 大量数据 */]'
```

### 5. 处理 JSON 数据

在 shell 中使用单引号包裹 JSON：
```bash
# 正确
--data '{"key": "value"}'

# 在双引号 shell 中可能有问题
--data "{\"key\": \"value\"}"
```

### 6. 查看执行计划

对于复杂查询，使用 EXPLAIN：
```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db execute \
  --sql 'EXPLAIN QUERY PLAN SELECT * FROM users WHERE age > 25'
```

## 常见问题

### Q: 数据库文件不存在怎么办？

**A**: 脚本会自动创建数据库文件。首次运行会创建空数据库。

### Q: WHERE 子句需要包含 WHERE 关键字吗？

**A**: 不需要。只提供条件部分，例如 `'age > ?'` 而不是 `'WHERE age > ?'`

### Q: 如何处理包含单引号的数据？

**A**: 使用参数化查询：
```bash
--where "name = ?" --params '["O'\''Brien"]'
```

### Q: 支持哪些 SQL 函数？

**A**: SQLite 支持标准 SQL 函数，如：
- 聚合: `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`
- 字符串: `LENGTH()`, `UPPER()`, `LOWER()`, `SUBSTR()`
- 日期: `DATE()`, `TIME()`, `DATETIME()`, `STRFTIME()`

### Q: 如何处理大型数据集？

**A**: 使用分页查询：
```bash
# 第一页（前 100 条）
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db query \
  --table users \
  --limit 100

# 使用 OFFSET（第二页）
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db execute \
  --sql 'SELECT * FROM users LIMIT 100 OFFSET 100'
```

### Q: 支持并发访问吗？

**A**: SQLite 支持多个读取者，但同时只能有一个写入者。对于高并发场景，考虑使用 PostgreSQL 或 MySQL。

## 错误处理

脚本会捕获并显示详细的错误信息：

```bash
# JSON 解析错误
错误：JSON 解析错误：Expecting property name enclosed in double quotes

# 数据库错误
数据库错误：no such table: users

# SQL 语法错误
数据库错误：near "SELEC": syntax error
```

## 性能提示

1. **创建索引** 加速查询：
```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db execute \
  --sql 'CREATE INDEX idx_user_email ON users(email)'
```

2. **批量操作** 比单条操作快得多：
```bash
# 慢：多次单条插入
# 快：一次批量插入
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db insert \
  --table users \
  --data '[/* 多条数据 */]'
```

3. **使用 EXPLAIN** 分析查询：
```bash
python3 skills/sqlite-db-ops/scripts/db_operations.py data.db execute \
  --sql 'EXPLAIN QUERY PLAN SELECT * FROM users WHERE email = "test@example.com"'
```

## 参考资源

- 完整文档: [`skills/sqlite-db-ops/SKILL.md`](../skills/sqlite-db-ops/SKILL.md)
- 脚本源码: [`db_operations.py`](../skills/sqlite-db-ops/scripts/db_operations.py)
- SQLite 官方文档: https://www.sqlite.org/docs.html
- SQLite 数据类型: https://www.sqlite.org/datatype3.html

---

**最后更新**: 2026-01-14
