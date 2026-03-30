#!/bin/bash
# Memory Archive Script - 记忆归档脚本
# 归档超过30天的记忆文件到 archive/ 目录

MEMORY_DIR="/Users/jiyingguo/.openclaw/workspace/memory"
ARCHIVE_DIR="$MEMORY_DIR/archive"
CURRENT_DATE=$(date +%s)
CUTOFF_DATE=$(date -v-30d +%s 2>/dev/null || date -d "30 days ago" +%s)

# 创建归档目录
mkdir -p "$ARCHIVE_DIR"

# 计算30天前的日期（用于日志）
CUTOFF_DATE_DISPLAY=$(date -v-30d +%Y-%m-%d 2>/dev/null || date -d "30 days ago" +%Y-%m-%d)
echo "归档截止日期: $CUTOFF_DATE_DISPLAY"
echo "开始归档30天前的记忆文件..."

# 统计变量
ARCHIVED_COUNT=0
ERROR_COUNT=0

# 遍历memory目录下的.md文件
for file in "$MEMORY_DIR"/*.md; do
    # 跳过archive目录本身
    if [[ "$file" == *"/archive/"* ]]; then
        continue
    fi
    
    # 获取文件修改时间
    if [[ -f "$file" ]]; then
        FILE_DATE=$(stat -f %m "$file" 2>/dev/null || stat -c %Y "$file" 2>/dev/null)
        
        # 如果文件超过30天
        if [ "$FILE_DATE" -lt "$CUTOFF_DATE" ]; then
            FILENAME=$(basename "$file")
            # 移动到archive目录
            mv "$file" "$ARCHIVE_DIR/" 2>/dev/null
            if [ $? -eq 0 ]; then
                echo "归档: $FILENAME"
                ARCHIVED_COUNT=$((ARCHIVED_COUNT + 1))
            else
                echo "错误: 无法归档 $FILENAME"
                ERROR_COUNT=$((ERROR_COUNT + 1))
            fi
        fi
    fi
done

echo ""
echo "归档完成! 共归档 $ARCHIVED_COUNT 个文件, $ERROR_COUNT 个错误"
echo "归档文件保存在: $ARCHIVE_DIR"
