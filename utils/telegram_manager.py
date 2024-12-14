import asyncio
from telethon import TelegramClient
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.errors import UserPrivacyRestrictedError

class TelegramManager:
    """
    A manager for handling Telegram client operations using Telethon.
    """

    def __init__(self, api_id, api_hash, phone, session_name='session_name'):
        """
        Initialize the TelegramManager.

        Args:
            api_id (int): Your Telegram API ID.
            api_hash (str): Your Telegram API Hash.
            phone (str): Your phone number associated with Telegram.
            session_name (str, optional): Name of the session file. Defaults to 'session_name'.
        """
        self.client = TelegramClient(session_name, api_id, api_hash)
        self.phone = phone

    async def start(self):
        """
        Start the Telegram client and authenticate the user.
        """
        await self.client.start(self.phone)
        user = await self.client.get_me()
        print(f"Authenticated as: {user.username}")

    async def disconnect(self):
        """
        Disconnect the Telegram client.
        """
        await self.client.disconnect()

    async def get_group(self, group_name):
        """
        Retrieve a Telegram group by its name.

        Args:
            group_name (str): The name of the group to retrieve.

        Returns:
            telethon.tl.types.Chat or None: The group entity if found, else None.
        """
        dialogs = await self.client.get_dialogs()
        for dialog in dialogs:
            if dialog.is_group and dialog.name == group_name:
                return dialog.entity
        return None

    async def get_participants(self, group):
        """
        Get all participants of a Telegram group.

        Args:
            group (telethon.tl.types.Chat): The group entity.

        Returns:
            list: A list of participant entities.
        """
        return await self.client.get_participants(group)

    async def add_user_to_group(self, target_group, user_entity, fwd_limit=100):
        """
        Add a user to a Telegram group.

        Args:
            target_group (telethon.tl.types.Chat): The target group entity.
            user_entity (telethon.tl.types.User): The user entity to add.
            fwd_limit (int, optional): Forward limit. Defaults to 100.

        Raises:
            UserPrivacyRestrictedError: If the user has privacy settings that prevent adding.
            Exception: For any other errors during the addition.
        """
        try:
            await self.client(AddChatUserRequest(
                chat_id=target_group.id,
                user_id=user_entity.id,
                fwd_limit=fwd_limit
            ))
            print(f"User {user_entity.id} ({user_entity.username}) added to '{target_group.title}'.")
            await asyncio.sleep(1)  # Delay of 1 second between additions
        except UserPrivacyRestrictedError:
            print(f"User {user_entity.id} has privacy settings that prevent adding to groups.")
        except Exception as e:
            print(f"Error adding user {user_entity.id}: {e}")