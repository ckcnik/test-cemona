from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save, pre_save
from cemona.models import Modem, LoggingModem
# from .models import Action, UserLesson, UserFriend, UserCategory

# TODO Доделать логирование
# def logging_modem(sender, instance, **kwargs):
#     """
#     Logging event added(change Probe) Modem to Probe
#     :param sender:
#     :param instance:
#     :param kwargs:
#     :return:
#     """
#
#     # если создаем нового пользователя
#     if not instance.id:
#         # instance.rank = Rank.objects.get(efficiency=12.5)  # привязываем к модели юзера начальный левел
#         # instance.username = instance.email  # подменяем логин на email
#         LoggingModem.objects.update_or_create(
#             probe=instance.probe,
#             action=action,
#             friend=instance,
#         )
#
#     if created:
#         try:
#             action = Action.objects.get(name='add_friend')
#             UserFriend.objects.update_or_create(
#                 user=instance.user,
#                 action=action,
#                 friend=instance,
#             )
#         except Action.DoesNotExist:
#             raise ObjectDoesNotExist('Action - "add_friend" does not exist')
#
# post_save.connect(logging_modem, dispatch_uid="change_Modem", sender=Modem)
