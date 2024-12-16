Some extra commands to learn after learning from the python file
A concise summary of the waiting commands where `asyncio` can switch tasks:


### **1. `asyncio.sleep()`**
- Pauses the coroutine, allowing the event loop to run other tasks.
  ```python
  await asyncio.sleep(2)  # Task switch
  ```


### **2. I/O Operations**
- Includes `asyncio.open_connection()`, `asyncio.StreamReader.read()`, etc., which switch tasks while waiting for I/O.
  ```python
  reader, writer = await asyncio.open_connection('example.com', 80)  # Task switch
  ```


### **3. Synchronization Primitives**
- `asyncio.Lock`, `asyncio.Queue`, and similar constructs cause task switches when waiting.
  ```python
  async with lock:  # Task switch if already locked
      await queue.get()  # Task switch if queue is empty
  ```


### **4. Timeout Functions**
- `asyncio.wait_for()` or `asyncio.wait()` switches tasks during the wait.
  ```python
  await asyncio.wait_for(some_coroutine(), timeout=5)  # Task switch
  await asyncio.wait([coro1(), coro2()])  # Task switch between coroutines
  ```


### **5. `asyncio.gather()`**
- Runs multiple coroutines concurrently, switching between them. returns the result in a list
  ```python
  await asyncio.gather(task1(), task2())  # Task switch , it doesn't have error handling
  ```


### **6. Futures**
- Task switches when awaiting unresolved `asyncio.Future`.
  ```python
  result = await future  # Task switch until resolved
  ```


### **7. `asyncio.Event`**
- Switches tasks while waiting for an event to be set.
  ```python
  await event.wait()  # Task switch
  ```

**General Rule**: `asyncio` switches tasks when `await` encounters an operation that yields control to the event loop.
