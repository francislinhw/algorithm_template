CXX := g++
CXXFLAGS := -fdiagnostics-color=always -g -std=c++14 \ 
  -I/opt/homebrew/Cellar/boost/1.86.0/include \
  -I/Users/francis/local/include \
  -I. \
  -isystem /opt/homebrew/include

LDFLAGS := -L/Users/francis/local/lib \
  -L/opt/homebrew/Cellar/boost/1.86.0/lib \
  -lQuantLib

SRC := $(wildcard *.cpp)
TARGET ?= app
OUT := bin/$(TARGET)

all: $(OUT)

$(OUT): $(SRC)
	@mkdir -p bin
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LDFLAGS)

clean:
	rm -rf bin
