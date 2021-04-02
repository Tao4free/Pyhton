# import logging
from threading import Event

from google.cloud import pubsub_v1

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

def nihao():
    print('nihao')

def callback(message, event):
    print(message)
    # logger.info(message)
    raise ValueError()
    # nihao()
    # event.set()


def main():
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path('ca-lutao-test', 'my-topic')

    event = Event()

    def callback_wrapper(message):
        callback(message, event)

    data = 'nihao'
    future = publisher.publish(topic_path, data.encode("utf-8"))
    future.add_done_callback(callback_wrapper('done'))
    # future = subscriber.subscribe('subscription/path', callback=callback_wrapper)

    print('after raise')

    # event.wait()
    # logger.exception('Got event. Shutting down.')
    # future.cancel()
    # exit(1)

if __name__ == "__main__":
    main()
