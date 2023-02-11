from progress.bar import Bar
import time
bar = Bar('Processing', max=100)
for i in range(100):
    time.sleep(0.01)
    # Do some work
    bar.next()
bar.finish()

# from progress.bar import Bar

# bar = Bar('Processing', max=20)
# for i in range(20):
#     # Do some work
#     bar.next()
# bar.finish()