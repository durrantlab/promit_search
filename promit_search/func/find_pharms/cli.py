
from .single_file import single_file
from .multi_file import multi_file

from promit_search.io import gen

def cli(args):
    """Will take in the cli input and run func correctly

    Args:
        args: input from command line interface
    """

    # determine if single or multifile
    try:
        gen.dir_verify(args.sdf_path, False)
        func = multi_file
    except FileNotFoundError:
        func = single_file 

    func(args.sdf_path, args.output_path, 
          args.create_dir, args.run_type)
