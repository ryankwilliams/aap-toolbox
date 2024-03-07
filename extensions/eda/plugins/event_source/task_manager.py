import asyncio
import aiohttp
from typing import Any, Dict


async def main(queue: asyncio.Queue, args: Dict[str, Any]) -> None:
    url = args.get("url")
    delay = args.get("delay", 30)

    while True:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url=f"{url}/api/tasks/") as response:
                    for task in await response.json():
                        if task["status"] != "todo":
                            continue

                        await queue.put(
                            {
                                "task_id": task["task_id"],
                                "name": task["name"],
                                "status": task["status"],
                            }
                        )

                        async with session.put(
                            url=f"{url}/api/tasks/{task['task_id']}",
                            json={"status": "in progress"},
                        ):
                            pass
        except aiohttp.ClientError as e:
            await queue.put({"error_msg": str(e)})

        await asyncio.sleep(delay)


if __name__ == "__main__":

    class MockQueue:
        async def put(self, event) -> None:
            print(event)

    asyncio.run(main(MockQueue(), dict(url="http://0.0.0.0:8080")))
