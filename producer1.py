import redis

r=redis.Redis('127.0.0.1')
r.flushdb()

key='numbers'

n=1

while n<=10 :
    data = {'n':n}
    msg_id=r.xadd(key,data)

    print('length: ',r.xlen(key))
    print('Memory Usage: ',r.memory_usage(key))
    print(f'Produced the number {n} as message id {msg_id}')

    n+=1