import timeit
import matplotlib.pyplot as plt
from program import HashTableApp

def setup_app():
    app = HashTableApp()
    # Setup with a predefined table size and students for consistent benchmarking
    app.table_size = 100
    for i in range(app.table_size):
        app.insert_hopscotch(f"student{i}", "1990-01-01")
    return app

def benchmark_search_student(app, iterations=1000):
    setup_code = f"""
from __main__ import setup_app
app = setup_app()
    """
    test_code = """
app.search_student(send_messagebox=False)
    """
    return timeit.timeit(test_code, setup=setup_code, number=iterations)

def benchmark_insert_hopscotch(app, iterations=1000):
    setup_code = f"""
from __main__ import setup_app
app = setup_app()
    """
    test_code = """
app.insert_hopscotch("new_student", "1990-01-01", send_messagebox=False)
    """
    return timeit.timeit(test_code, setup=setup_code, number=iterations)

def benchmark_insert_cuckoo(app, iterations=1000):
    setup_code = f"""
from __main__ import setup_app
app = setup_app()
    """
    test_code = """
app.insert_cuckoo("new_student", "1990-01-01", send_messagebox=False)
    """
    return timeit.timeit(test_code, setup=setup_code, number=iterations)

def benchmark_clear_student(app, iterations=1000):
    setup_code = f"""
from __main__ import setup_app
app = setup_app()
    """
    test_code = """
app.clear_student(send_messagebox=False)
    """
    return timeit.timeit(test_code, setup=setup_code, number=iterations)

if __name__ == "__main__":
    app = setup_app()
    sizes = [100, 200, 300, 400, 500]
    search_times = []
    insert_hopscotch_times = []
    insert_cuckoo_times = []
    clear_student_times = []

    for size in sizes:
        app.table_size = size
        search_time = benchmark_search_student(app)
        insert_hopscotch_time = benchmark_insert_hopscotch(app)
        insert_cuckoo_time = benchmark_insert_cuckoo(app)
        clear_student_time = benchmark_clear_student(app)

        search_times.append(search_time)
        insert_hopscotch_times.append(insert_hopscotch_time)
        insert_cuckoo_times.append(insert_cuckoo_time)
        clear_student_times.append(clear_student_time)
    
    theoretical_times = []
    base_size = sizes[0]
    base_time = 1  
    scaling_factor = 0.01

    for size in sizes:
        ratio = (size / base_size) ** 2
        time = base_time * ratio * scaling_factor
        theoretical_times.append(time)

    plt.plot(sizes, theoretical_times, label="O(n^2)")
    plt.plot(sizes, search_times, label="Search Student")
    plt.plot(sizes, insert_hopscotch_times, label="Insert Hopscotch")
    plt.plot(sizes, insert_cuckoo_times, label="Insert Cuckoo")
    plt.plot(sizes, clear_student_times, label="Clear Student")
    plt.legend()
    plt.show()
