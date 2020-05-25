import rx
from rx import operators as ops

words = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]


clock_source = rx.interval(1.0)

composed = clock_source.pipe(
    ops.map(lambda i: words[i % len(words)]),
    ops.map(lambda s: len(s)),
    ops.filter(lambda i: i >= 5),
)
composed.subscribe(lambda value: print("Received {0}".format(value)))

input("Press any key to exit")