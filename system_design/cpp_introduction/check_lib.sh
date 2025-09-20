#!/bin/bash
# 📦 C++ 套件檢查工具
# 用法: ./check_lib.sh <套件名> <include路徑> <lib路徑>

PKG=$1
INCLUDE=$2
LIB=$3

if [ -z "$PKG" ] || [ -z "$INCLUDE" ] || [ -z "$LIB" ]; then
  echo "用法: $0 <套件名> <include路徑> <lib路徑>"
  echo "例子: $0 QuantLib /usr/local/include /usr/local/lib"
  exit 1
fi

echo "🔍 Step 1. 檢查 header..."
echo "#include <$PKG>" | g++ -E -I$INCLUDE -xc++ - -o /dev/null
if [ $? -ne 0 ]; then
  echo "❌ 找不到 header，請檢查 -I 參數 ($INCLUDE)"
  exit 1
else
  echo "✅ header OK"
fi

echo ""
echo "🔍 Step 2. 檢查 library..."
LIBFILES=$(ls $LIB 2>/dev/null | grep -i $PKG)
if [ -z "$LIBFILES" ]; then
  echo "📂 沒找到 lib 檔案，看起來是 header-only"
else
  echo "📂 找到以下 lib 檔案:"
  echo "$LIBFILES"
fi

echo ""
echo "🔍 Step 3. 測試 link..."
cat > test_$PKG.cpp <<EOF
#include <$PKG>
int main() { return 0; }
EOF

g++ test_$PKG.cpp -I$INCLUDE -L$LIB -l$PKG -o test_$PKG.out 2>/dev/null
if [ $? -ne 0 ]; then
  echo "⚠️ Link 失敗，可能 -l$PKG 不對，請檢查 library 名稱"
else
  echo "✅ Link OK (生成 test_$PKG.out)"
fi

rm -f test_$PKG.cpp
