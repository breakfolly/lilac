if !has('python3')
    echo "Error: Lilac requires vim compiled with +python3"
    finish
endif

let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

command! -nargs=* Lilac python3 command(<f-args>)

python3 << EOF

import sys
from os.path import normpath, join
import vim
plugin_root_dir = vim.eval('s:plugin_root_dir')
sys.path.insert(0, plugin_root_dir)
LilacPyPath = plugin_root_dir + "/lilac.py"
import lilac

def command(arg1, arg2="127.0.0.1", arg3="1111", arg4="user"):
	if arg1 == "connect":
		lilac.LilacClient(arg2, arg3, arg4)
	elif arg1 == "start":	
		vim.command(':silent execute "!' + LilacPyPath + ' ' + arg3 + ' ' + arg4 + '&>/dev/null &" | execute ":redraw!"')
	#	vim.command(':silent execute "!' + LilacPyPath + ' ' + arg3 + ' ' + arg4 + '" | execute ":redraw!"')
	elif arg1 == "quit":
	    lilac.LilacServer.quit()

EOF

function! Sample()
	python3 lilac.print_test()
endfunction

