
import pprint

def print_csv(results, options, _):
    csv_output(list(results), options.verbose)
    return 0

def csv_output(result, verbose):
    print "NLOC,CCN,token,PARAM,length,location,file,function,start,end"
    for source_file in result:
        if source_file:
            for source_function in source_file.function_list:
                if source_function:
                    print('{},{},{},{},{},"{}","{}","{}","{}"'.format(
                        source_function.nloc,
                        source_function.cyclomatic_complexity,
                        source_function.token_count,
                        len(source_function.parameters),
                        source_function.end_line - source_function.start_line,
                        "{}@{}-{}@{}".format(
                            source_function.name,
                            source_function.start_line,
                            source_function.end_line,
                            source_file.filename
                        ),
                        source_file.filename,
                        source_function.name,
                        source_function.start_line,
                        source_function.end_line
                    ))
