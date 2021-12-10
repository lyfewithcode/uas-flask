from blogs import app, conn
from flask import render_template, request, redirect, url_for, flash

global session, pengguna
session = False
pengguna = ''


@app.route('/')
@app.route("/home")
def home_page():
    sql = "SELECT * FROM post ORDER BY idpost DESC"

    cursor = conn.cursor()
    cursor.execute(sql)

    artikel = cursor.fetchall()

    return render_template('index.html', artikel=artikel, session=session, pengguna=pengguna)


@app.route('/blog', methods=['GET', 'POST'])
def blog_page():
    # Mengubah data
    _idTemp = request.values.get('temp_id')
    _judul = request.values.get('judul')
    _isi = request.values.get('isi')
    _keyword = request.values.get('keyword')

    sql_ubah = "UPDATE post SET judul=%s, isi=%s, keyword=%s WHERE idpost=%s"
    data_ubah = (_judul, _isi, _keyword, _idTemp)
    cursor_ubah = conn.cursor()
    cursor_ubah.execute(sql_ubah, data_ubah)
    conn.commit()

    redirect(url_for('blog_page'))

    # Menampilkan data
    sql_tampil = "SELECT * FROM post ORDER BY idpost DESC"

    cursor_tampil = conn.cursor()
    cursor_tampil.execute(sql_tampil)

    artikel = cursor_tampil.fetchall()

    if not session:
        return redirect(url_for('login_page'))

    else:
        return render_template('blog.html', artikel=artikel, session=session, pengguna=pengguna)


@app.route('/blog/hapus/<_id>')
def hapus_data(_id):
    sql = "DELETE FROM post WHERE idpost = %s"
    data = _id
    cursor = conn.cursor()
    cursor.execute(sql, data)
    conn.commit()

    return redirect(url_for('blog_page'))


@app.route('/blog/tambah', methods=['POST'])
def tambah_data():
    if request.method == 'POST':
        # Menambah data
        _judul = request.values.get('judul_post')
        _isi = request.values.get('isi_post')
        _keyword = request.values.get('keyword_post')

        sql = "INSERT INTO post VALUES (null, %s, %s, %s)"
        data = (_judul, _isi, _keyword)

        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()

        return redirect('/blog')
    else:
        return render_template('blog.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    _username = request.values.get('username')
    _password = request.values.get('password')

    if request.method == 'POST':
        sql = 'SELECT * FROM pengguna WHERE username=%s'

        cursor = conn.cursor()
        cursor.execute(sql, _username)
        hasil = cursor.fetchone()
        akun_cek = cursor.rowcount

        if akun_cek != 0 and _username == hasil[2] and _password == hasil[3]:
            global session, pengguna
            session = True
            pengguna = hasil[1]

            flash(f'Anda login sebagai {pengguna}', category='success')
            return redirect(url_for("home_page"))
        elif not hasil:
            flash(f'Akun tidak tersedia', category='danger')
            return redirect(url_for('login_page'))
        else:
            flash(f'Gagal, tolong periksa kembali', category='danger')
            return redirect(url_for("login_page"))
    else:
        return render_template('login.html')


@app.route('/user', methods=['GET', 'POST'])
def user_page():
    # Mengubah data
    _idTemp = request.values.get('temp_id')
    _userTemp = request.values.get('temp_user')
    _username = request.values.get('username')
    _password = request.values.get('password')

    sql_ubah = "UPDATE pengguna SET namalengkap=%s, username=%s, password=%s WHERE iduser=%s"
    data_ubah = (_userTemp, _username, _password, _idTemp)
    cursor_ubah = conn.cursor()
    cursor_ubah.execute(sql_ubah, data_ubah)
    conn.commit()

    redirect(url_for('user_page'))

    # Menampilkan data
    sql = "SELECT * FROM pengguna ORDER BY iduser DESC"

    cursor_tampil = conn.cursor()
    cursor_tampil.execute(sql)

    user = cursor_tampil.fetchall()

    if not session:
        return redirect(url_for('login_page'))

    else:
        return render_template('user.html', session=session, pengguna=pengguna, user=user)


@app.route('/user/tambah', methods=['POST'])
def tambah_user():
    if request.method == 'POST':
        # Menambah data
        _user = request.values.get('pemakai')
        _username = request.values.get('username')
        _password = request.values.get('password')

        if len(_user) <= 40 and len(_username) <= 6 and len(_password) <= 6:
            sql = "INSERT INTO pengguna VALUES (null, %s, %s, %s)"
            data = (_user, _username, _password)

            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()

            return redirect(url_for('user_page'))
        else:
            flash(f'Jumlah karakter melebihi batas', category='danger')
            return redirect(url_for('user_page'))
    else:
        return render_template('blog.html')


@app.route('/user/hapus/<_id>/<_user>')
def hapus_user(_id, _user):
    sql = "DELETE FROM pengguna WHERE iduser = %s"
    data = _id
    cursor = conn.cursor()
    cursor.execute(sql, data)
    conn.commit()

    if _user == pengguna:
        return redirect(url_for('logout_session'))

    else:
        return redirect(url_for('user_page'))


@app.route('/logout')
def logout_session():
    global session, pengguna
    session = False
    pengguna = ''

    flash(f'Anda telah keluar', category='warning')
    return redirect(url_for("home_page"))
