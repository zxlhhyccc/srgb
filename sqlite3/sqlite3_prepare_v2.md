是的，您可以使用 `sqlite3_prepare_v2`、`sqlite3_step` 和 `sqlite3_finalize` 函数来查询数据，而不使用回调函数。这种方法允许更细致地控制查询过程。

### 使用 `sqlite3_prepare_v2` 查询数据的步骤

1. **准备 SQL 语句**
2. **执行 SQL 语句**
3. **获取结果**
4. **清理资源**

### 示例代码

以下是一个使用这种方法的完整示例：

```c
#include <stdio.h>
#include <sqlite3.h>

int main() {
    sqlite3 *db;
    sqlite3_stmt *stmt;
    const char *sql = "SELECT * FROM your_table;";
    int rc;

    // 打开数据库
    rc = sqlite3_open("example.db", &db);
    if (rc) {
        fprintf(stderr, "Can't open database: %s\n", sqlite3_errmsg(db));
        return 1;
    }

    // 准备 SQL 语句
    rc = sqlite3_prepare_v2(db, sql, -1, &stmt, 0);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "Failed to prepare statement: %s\n", sqlite3_errmsg(db));
        return 1;
    }

    // 执行 SQL 语句并获取结果
    while ((rc = sqlite3_step(stmt)) == SQLITE_ROW) {
        int id = sqlite3_column_int(stmt, 0); // 假设第一列是整数类型
        const char *name = (const char *)sqlite3_column_text(stmt, 1); // 假设第二列是文本类型
        printf("ID: %d, Name: %s\n", id, name);
    }

    // 检查执行结果
    if (rc != SQLITE_DONE) {
        fprintf(stderr, "Execution failed: %s\n", sqlite3_errmsg(db));
    }

    // 清理资源
    sqlite3_finalize(stmt);
    sqlite3_close(db);

    return 0;
}
```

### 说明

- **`sqlite3_prepare_v2`**：准备 SQL 语句，返回一个 `sqlite3_stmt` 指针。
- **`sqlite3_step`**：执行 SQL 语句，返回当前行的状态。
- **`sqlite3_column_*`**：获取列的数据，您可以根据列的类型选择合适的方法。
- **`sqlite3_finalize`**：释放准备好的 SQL 语句资源。

这种方法适用于需要更复杂处理的场景，允许您逐行处理结果。