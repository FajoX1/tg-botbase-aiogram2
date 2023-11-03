import aiosqlite

async def insert(user):
    async with aiosqlite.connect("./database/data/users.db") as db:
        async with db.execute("SELECT id FROM users WHERE id=?", (user.id,)) as cursor:
            existing_user = await cursor.fetchone()
            if existing_user is None:
                await db.execute("INSERT INTO users (id, first_name, last_name, username, blocked) VALUES (?, ?, ?, ?, ?)",
                                (user.id, user.first_name, user.last_name, user.username, 0))
                await db.commit()

async def get_user(user):
    async with aiosqlite.connect("./database/data/users.db") as db:
        async with db.execute("SELECT * FROM users WHERE id=?", (user.id,)) as cursor:
            user_data = await cursor.fetchone()
            user_db = {
                    "id": user_data[0],
                    "first_name": user_data[1],
                    "last_name": user_data[2],
                    "username": user_data[3],
                    "blocked": user_data[6],
                }
            return user_db