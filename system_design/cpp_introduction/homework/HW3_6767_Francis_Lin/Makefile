CXX := g++ 
CXXFLAGS := -fdiagnostics-color=always -g -std=c++11 \
  -I/opt/homebrew/Cellar/boost/1.86.0/include \
  -I/Users/francis/local/include \
  -I. \
  -isystem /opt/homebrew/include

LDFLAGS := -L/Users/francis/local/lib \
  -L/opt/homebrew/Cellar/boost/1.86.0/lib \
  -lQuantLib

# All source files
SRC_UTIL := Option.cpp Option_Price.cpp
SRC_MAIN := main.cpp $(SRC_UTIL)
SRC_TEST := unit_test/unit_test.cpp $(SRC_UTIL)

BIN_DIR := bin
MAIN := $(BIN_DIR)/main
TEST := $(BIN_DIR)/unit_test

.PHONY: all clean main test

all: $(MAIN) $(TEST)

main: $(MAIN)
test: $(TEST)

$(MAIN): $(SRC_MAIN)
	@mkdir -p $(BIN_DIR)
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LDFLAGS)

$(TEST): $(SRC_TEST)
	@mkdir -p $(BIN_DIR)
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LDFLAGS)

clean:
	rm -rf $(BIN_DIR)
