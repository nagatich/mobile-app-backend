from django.db.models.signals import post_save
from django.dispatch import receiver

from notifications.tasks import notificate_by_ws

from ..models import WishListItem
from ..serializers import WishListItemSerializer
from ..events import NEW_WISH_LIST_ITEM, WISH_LIST

@receiver(post_save, sender=WishListItem)
def new_wish_list_item(sender, instance, created, **kwargs):
    if created:
        room = f'{instance.user.username}_{WISH_LIST}'
        data = WishListItemSerializer(instance=instance)
        notificate_by_ws.delay(
            room=room,
            message=None,
            event=NEW_WISH_LIST_ITEM,
            data=data
        )
