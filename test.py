import asyncio
async def main():
    print("start")
    await asyncio.sleep(4)
    print("end")

asyncio.run(main)