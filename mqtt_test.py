import paho.mqtt.client as mqtt

'''
[SERVER COMMANDS]
mosquitto_pub -t "/test" -m "exit"
'''


def on_connect(client, userdata, flags, rc):
    print(f'Connected with resuls: {str(rc)}')
    client.subscribe('/test')


def on_message(client, userdata, msg):
    # print(msg.payload.decode('utf-8'))

    if msg.payload.decode('utf-8') == 'bathroom':
        # Add functional code..
        print('Switching bathroom lights...')
        pass

    elif msg.payload.decode('utf-8') == 'exit':
        print('Exiting, disconnecting client...')
        client.disconnect()

    else:
        print('Unsupported command, try again')


cli = mqtt.Client()
cli.on_connect = on_connect
cli.on_message = on_message
cli.connect("172.105.76.166", 1883, 10)
cli.loop_forever()
