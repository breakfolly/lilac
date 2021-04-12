if !has('python3')
    echo "Error: Lilac requires vim compiled with +python3"
    finish
endif

let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python3 << EOF

import sys
from os.path import normpath, join
import vim
plugin_root_dir = vim.eval('s:plugin_root_dir')
sys.path.insert(0, plugin_root_dir)
import lilac

EOF

function! Sample()
	python3 lilac.print_test()
endfunction
