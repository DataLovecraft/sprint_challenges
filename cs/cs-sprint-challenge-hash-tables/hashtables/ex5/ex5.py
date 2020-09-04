



def finder(files, queries):
    """
    Given a list of full paths to files, and a list of filenames to query,
    report all the full paths that match that filename.

    Args:

    Returns:


    """
    # init empty dict:
    cache = {}
    # init empty list for results:
    result = []

    # loop over all the paths in files and split filename:
    for path in files:
        query = path.split('/')[-1]
        print(query)

    # if file is in the cache
    # append current path to index:
    if query in cache:
        cache[query].append(path)

    # else add query as the key
    # and the path as the value in the cache:
    else:
        cache[query] = [path]

    # Next we loop over each file in the query list
    # to check if query is present the cache
    # if its present, add the path value to the results list:
    for query in queries:
        if query in cache:
            results = cache[query]
            # for each path in the results, append the results list.
            for path in results:
                result.append(path)


    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
