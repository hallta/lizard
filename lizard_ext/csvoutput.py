
def print_csv(results, options, _):
    print(csv_output(list(results), options.verbose))
    return 0

def csv_output(result, verbose):
    for source_file in result:
        if source_file:
            print source_file.filename

