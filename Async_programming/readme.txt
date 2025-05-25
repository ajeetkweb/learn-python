In synchronous programming,
 tasks are executed sequentially, with each task waiting for the previous one 
 to complete before proceeding. 

   Each task waits for the previous task to finish.

   Slow if tasks involve waiting (e.g., sleep, I/O).

🔹 What Is Asynchronous Programming?
     asynchronous tasks can run concurrently, utilizing resources more efficiently 
     and enhancing responsiveness in applications.

     With asyncio:

        Tasks yield control while waiting.

        Other tasks run in the meantime — concurrent execution.


Concept	                         Description

async def	                     Declares a coroutine function.

await	                         Waits for the result of a coroutine.

asyncio.run()	                 Starts the event loop.

asyncio.sleep()	                 Non-blocking sleep.

asyncio.create_task()	         Schedules concurrent coroutines.