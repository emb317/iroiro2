# 実行ファイル名
PROG := a.exe

# オブジェクトの出力先
OUTDIR := obj

# インクルードパス
INCDIR += -I src/inc
INCDIR += -I src/inc2

# ソース (ファイルパスを指定する)
SRCS += src/main.c
# ソース (特定のフォルダ内すべてをコンパイル対象とする場合)
SRCS += $(wildcard src/test/*.c)

# 使用するコンパイラ
CC = gcc
# コンパイルオプション
CFLAGS = -Wall -O2 $(INCDIR) -g

RM = cmd.exe /C del /F

# ------ ここより下は変更しないこと! ------
OBJS := $(addprefix $(OUTDIR)/,$(notdir $(patsubst %.c,%.o,$(SRCS))))
DEPS := $(addprefix $(OUTDIR)/,$(notdir $(patsubst %.c,%.d,$(SRCS))))
VPATH = $(OUTDIR) $(dir $(SRCS))

$(PROG): $(OBJS) $(DEPS)
	$(CC) -o $@ $(OBJS)

$(OUTDIR)/%.d:%.c
	$(CC) $(CFLAGS) -MM $< | sed 's!.*:!$(patsubst %.d,%.o,$@):!' > $@

$(OUTDIR)/%.o:%.c
	$(CC) $(CFLAGS) -c -o $@ $<

.PHONY : clean depend
clean:
	$(RM) $(PROG)
	$(RM) $(OUTDIR)/*.*

-include $(DEPS)
