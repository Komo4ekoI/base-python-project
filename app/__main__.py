from app import log

log.setup()


async def main():
    print("Hello, world!")


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
