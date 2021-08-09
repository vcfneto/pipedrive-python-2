class Webhooks(object):
    def __init__(self, client):
        self._client = client

    def get_hooks_subscription(self, **kwargs):
        url = 'webhooks'
        return self._client._get(url, **kwargs)

    def create_hook_subscription(self, subscription_url, event_action, event_object, **kwargs):
        url = 'webhooks'
        data = {
            'subscription_url':
                subscription_url,
            'event_action': event_action,
            'event_object': event_object
        }
        return self._client._post(url, json=data, **kwargs)

    def delete_hook_subscription(self, hook_id, **kwargs):
        url = 'webhooks/{}'.format(hook_id)
        return self._client._delete(url, **kwargs)
