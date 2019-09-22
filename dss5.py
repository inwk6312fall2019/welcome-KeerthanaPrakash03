import random, time

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, s.count(c))
    return d

def sum_dict_values(*t):
    return sum(t)

def choose_from_hist(h):
    print(h)
    random_key = random.choice(list(h.keys()))
    probability = h[random_key]/sum(h.values())
    values_sum = sum(h.values())
    print('Random value is "{}" and its probability is {}/{}, i.e. {}.' \
          .format(random_key, h[random_key], sum(h.values()), probability))
    
start_time = time.time()
#h=histogram('brontosaurus')
h=histogram('aba')
choose_from_hist(h)
function_time = time.time() - start_time

print('\nRunning time is {0:.4f} s'.format(function_time))
