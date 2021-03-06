##
# Project Title
#
# @file
# @version 0.1

BIN	=	pbrain-gomoku-ai

SRC	=	pbrain-gomoku-ai.py

RM	=	rm -rf

all:
	cp $(SRC) $(BIN)
	chmod +x $(BIN)

clean:
	$(RM) $(BIN)

fclean:	clean


re:	fclean all
# end
