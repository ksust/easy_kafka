easy_kafka
^^^^^^^^^^
Easy to use python kafka(for kb first)

As a message queue, Kafka has the following characteristics:

* Stable, No data loss.
* Save sent messages.
* Allow larger data.
* Allow slower speed.


Quick Start
-----------
**Installation**: pip install easy_kafka

1.config
>>>>>>>>
Edit conf/conf.yml
::

    kafka: # kafka config
      bootstrap_servers: 127.0.0.1:9092 # kafka servers, multiple, 172.1.0.2:9092,172.1.0.1:9092
      group_id: group # consumer group
      topic_subscribe: # topic, multiple
        - topic1
        - topic2
      topic_produce: topic1_result # producer default topic

2.demo-consumer
>>>>>>>>>>>>>>>>>>
::

    import json
    from easy_kafka.kafka_consumer import EasyKafkaConsumer

    def start_consumer():
        kafka_consumer = EasyKafkaConsumer('conf/conf.yml')
        print('consumer iterator started')
        for record in kafka_consumer:
            print('record', record.value)
            print('json', json.loads(record.value))

    if __name__ == "__main__":
        start_consumer()

3.demo-consumer-callback
>>>>>>>>>>>>>>>>>>>>>>>>>
::

    import json
    from easy_kafka.kafka_consumer import EasyKafkaConsumer
    from easy_kafka.kafka_producer import EasyKafkaProducer

    kafka_producer = EasyKafkaProducer('conf/conf.yml')

    def consumer_task(record):
        """
        consumer callback
        :param record: object
        :return:
        """
        print('consumer_task', record.value)
        print('json', json.loads(record.value))
        if record.topic is 'topic1':
            kafka_producer.produce_msg({'type': 'task result'})

    def start_consumer():
        kafka_consumer = EasyKafkaConsumer('../conf/conf.yml')
        print('consumer task started')
        kafka_consumer.subscribe(fn=consumer_task)

    if __name__ == "__main__":
        start_consumer()

4.demo-producer
>>>>>>>>>>>>>>>>>>>>>>>>>
::

    from easy_kafka.kafka_config import EasyKafkaConfig
    from easy_kafka.kafka_producer import EasyKafkaProducer

    def demo_produce_msg():
        kafka_producer = EasyKafkaProducer('conf/conf.yml')
        kafka_producer.produce_msg({'name': 'ksust'})

    def demo_produce_msg_with_config():
        config = EasyKafkaConfig('conf/conf.yml')
        print('config', config.__dict__)
        kafka_producer = EasyKafkaProducer(config)
        kafka_producer.produce_msg({'name': 'ksust'})
        kafka_producer.produce_msg_topic('topic1', {'name': 'ksust'})

    if __name__ == "__main__":
        demo_produce_msg()
        demo_produce_msg_with_config()
