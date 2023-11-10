# from cmd import Cmd
import cmd


class CommandLine(cmd.Cmd):
    prompt = "$ "

    def do_salam(self, arg):
        """ quite / exit commands"""
        return True
    # aliasing 4Ex making another command for exit
    # declaring variable do_exit then assign exit function to it
    do_exit = do_salam
    do_kudashi = do_salam
    # all of those aliases pointing k same location


command = CommandLine()
command.cmdloop()

# if __name__ == "__main__":
#     inst1 = CommandLine
#     print()
#     print(f"cmd module: \n {dir(Cmd)}")
#     print(f"cmd class:\n {dir(CommandLine)}")
#     print(f"inst of cmd class:\n {dir(inst1)}")
# ss
