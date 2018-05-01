import pymysql

tasks_list = []
ID_list = []


def init():
    # initialize the task list
    try:
        # open the file
        #txt = open(filename)

        global tasks_list
        global ID_list

        #SQL
        connection = pymysql.connect(user="root",password="dodo",database="lab5",host="localhost")
        sql = "SELECT todo,id FROM task WHERE done=0;"
        #sql = "SELECT * FROM task;"
        cursor = connection.cursor()
        cursor.execute(sql)
        tuple = cursor.fetchall()
        for tupla in tuple:
            tasks_list.append(tupla[0])
            ID_list.append(tupla[1])
        cursor.close()
        connection.close()
        #fine sql
    except IOError:
        # File not found! We work with an empty list
        print("File not found!")
    return

def checkPresente(testo):
    connection = pymysql.connect(user="root", password="dodo", database="lab5", host="localhost")
    cursor = connection.cursor()
    sql = """SELECT id
        FROM task
        WHERE (todo=%s) AND (done=0);"""
    #cursor=connection.cursor()
    cursor.execute(sql, (testo,))
    primo = cursor.fetchone()
    cursor.close()
    connection.close()
    if primo != None:
        return primo[0]
    return -1


def newTask(testo):
    connection = pymysql.connect(user="root",password="dodo",database="lab5",host="localhost")
    cursor = connection.cursor()
    trovato = checkPresente(testo)
    if trovato == -1:
        sql = """
        INSERT INTO task(todo,done)
        VALUES (%s,FALSE)
        """
        cursor.execute(sql, (testo,) )
        tasks_list.append(testo)
        sql = """SELECT id
        FROM task
        WHERE done=0 AND todo=%s"""
        cursor.execute(sql, (testo,))
        tupla = cursor.fetchone()
        ID_list.append(tupla[0])
        print(tupla[0])
        connection.commit()
        ritorno=0
    else:
        ritorno=-1
    cursor.close()
    connection.close()
    return ritorno

def showTasks():
    return tasks_list

def parallelIDs():
    return ID_list

def removeTask(testo):

    global tasks_list
    global ID_list

    connection = pymysql.connect(user="root",password="dodo",database="lab5",host="localhost")
    presente = checkPresente(testo)
    cursor = connection.cursor()
    if presente!=-1:
        sql = """
        UPDATE task
        SET done = 1
        WHERE todo = %s
        """
        cursor.execute(sql, (testo,) )
        connection.commit()
        ritorno = 0
    else:
        ritorno = -1
    cursor.close()
    connection.close()

    tr=0
    i=0
    N = len(tasks_list)
    while tr==0 and i<N:
        if tasks_list[i]==testo:
            tr=1
        else:
            i=i+1

    del(ID_list[i])
    del(tasks_list[i])
    #tasks_list.remove(testo)
    #else:
    #errore
    return ritorno


def UpdateTaskByMap(desired):

    global tasks_list
    global ID_list

    conn = pymysql.connect(user="root",password="dodo",database="lab5",host="localhost")
    cur = conn.cursor()
    sql = """UPDATE task
    SET todo=%s
    WHERE id=%s
    """
    name = desired["id"]
    nuovoTodo = desired["todo"]
    sqlTest = """SELECT todo
    FROM task
    WHERE id=%s
    """
    cur.execute(sqlTest, (name,))
    res = (cur.fetchone())[0]
    if res!=None:
        cur.execute(sql, (nuovoTodo,name))
        conn.commit()
        ritorno = 0
        sql = """SELECT todo
        FROM task
        WHERE done=0"""
        cur.execute(sql)
        tuple = cur.fetchall()
        tasks_list = []
        for tupla in tuple:
            tasks_list.append(tupla[0])
    else:
        ritorno = -1
    cur.close()
    conn.close()
    return ritorno


def removeTaskByID(ID):
    connection = pymysql.connect(user="root", password="dodo", database="lab5", host="localhost")
    cur = connection.cursor()
    sql = """UPDATE task
    SET done = 1
    WHERE id=%s
    """
    cur.execute(sql, (ID,) )
    connection.commit()
    cur.close()
    connection.close()

    tr=0
    i=0
    N = len(tasks_list)
    while i<N and tr==0:
        if ID_list[i]==int(ID):
            tr=1
        else:
            i=i+1
    print(i)
    del(ID_list[i])
    del(tasks_list[i])
    return

if __name__ == '__main__':
    # main program
    #newTask("suca scemo")
    init()
    print(tasks_list)
    print(ID_list)
    #removeTaskByID(15)
    #print(tasks_list)
    #removeTaskByID(11)
    #print(tasks_list)
