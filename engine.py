import asyncio


class Engine:
    def __init__(self):
        self.id = "hPrsVzB9kFNR"
        self.queue = []

    async def nusx(self, item):
        await asyncio.sleep(0)
        self.queue.append(item)
        return len(self.queue)


async def main():
    obj = Engine()
    for i in range(5):
        await obj.nusx(i)
    print(obj.queue)


if __name__ == "__main__":
    asyncio.run(main())
