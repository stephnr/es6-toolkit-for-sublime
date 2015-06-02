import os
import sublime
import subprocess
import sublime_plugin

# =========================================================================== #


def execute_sh(*args):
    output = ''
    proc = subprocess.Popen(list(args), stdout=subprocess.PIPE, shell=True)
    for line in proc.stdout:
        line = line.decode('UTF-8')
        output += line
    return output


def babel_exists():
    if len(execute_sh('where', 'babel')) > 0:
        return True
    else:
        sublime.error_message('Babel is not installed on your system')
        return False


def check_js_file(filename):
    return True if filename.endswith('.js') else False

# =========================================================================== #


def compile(js_file, open_as_new_file=False):
    compiled_js = ''
    os.chdir(os.path.dirname(js_file))
    # Compile the JS File
    compiled_js = execute_sh('babel', os.path.basename(js_file))
    # Should we export this into a new file?
    if(open_as_new_file):
        new_view = sublime.active_window().new_file()
        new_view.run_command('toolkit_dump_js',
                             {'compiled_js': compiled_js})
    return compiled_js

# =========================================================================== #
# =========================================================================== #


class ES6_Toolkit_Dump_JS(sublime_plugin.TextCommand):
    def execute(self, edit, compiled_js):
        view = sublime.active_window().active_view()
        view.insert(edit, 0, compiled_js)
        view.set_syntax_file('Packages/JavaScript/JavaScript.tmLanguage')


class ES6_Toolkit_Compile_File(sublime_plugin.WindowCommand):
    def execute(self):
        view = self.window.active_view()
        # Continue if JS and Babel exists
        if(check_js_file(view.file_name()) is False and
           babel_exists()):
            sublime.error_message(os.path.basename(
                                  view.file_name()) +
                                  ' is not a valid JS File')
            return
        else:
            compile(view.file_name(), open_as_new_file=True)
