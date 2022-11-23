function getDetail(detailId, jenisPromo, namaPromo) {
    $.ajax({
        type: "POST",
        url: `daftar-promo/detail/${detailId}`,
        success: function(data) {
            if (jenisPromo == "Promo Hari Spesial") {
                $('#detailModalBody').html(`
                <table>
                    <tr>
                        <th>Jenis Promosi :</th>
                        <td>${jenisPromo}</td>
                    </tr>
                    <tr>
                        <th>Nama Promosi :</th>
                        <td>${namaPromo}</td>
                    </tr>
                    <tr>
                        <th>Diskon :</th>
                        <td>${data.discount}%</td>
                    </tr>
                    <tr>
                        <th>Tanggal Berlangsung :</th>
                        <td>${data.returns}</td>
                    </tr>
                </table>
                `);
            } else if (jenisPromo == "Promo Minimum Transaksi") {
                $('#detailModalBody').html(`
                <table>
                    <tr>
                        <th>Jenis Promosi :</th>
                        <td>${jenisPromo}</td>
                    </tr>
                    <tr>
                        <th>Nama Promosi :</th>
                        <td>${namaPromo}</td>
                    </tr>
                    <tr>
                        <th>Diskon :</th>
                        <td>${data.discount}%</td>
                    </tr>
                    <tr>
                        <th>Minimum Transaksi :</th>
                        <td>${data.returns}</td>
                    </tr>
                </table>
                `);
            }
        }
    });
}

function addEntry(editId, jenisPromo, namaPromo) {
    if (jenisPromo == "Promo Hari Spesial") {
        $('#form-ubah-promo').html(`
            <fieldset disabled>
                <div class="form-outline mb-4">
                    <label for="jenisPromosi" class="form-label">Jenis Promosi</label>
                    <input type="text" id="jenisPromosi" class="form-control" placeholder="${jenisPromo}">
                </div>
                <div class="form-outline mb-4">
                    <label for="namaPromosi" class="form-label">Nama Promosi</label>
                    <input type="text" id="namaPromosi" class="form-control" placeholder="${namaPromo}">
                </div>
            </fieldset>
            <div class="form-outline mb-4">
                <label class="form-label">Diskon (dalam %)</label>
                <input id="diskon-hari" class="form-control" type="number" name="nama"></input>
            </div>
        `);

        $('#ubahModalFooter').html(`                
        <button type="button" class="btn btn-outline-success" data-bs-dismiss="modal" onclick="ubahPromoHariSpesial('${editId}')">Simpan</button>
        `);
    } else if (jenisPromo == "Promo Minimum Transaksi") {
        $('#form-ubah-promo').html(`
            <fieldset disabled>
                <div class="form-outline mb-4">
                    <label for="jenisPromosi" class="form-label">Jenis Promosi</label>
                    <input type="text" id="jenisPromosi" class="form-control" placeholder="${jenisPromo}">
                </div>
                <div class="form-outline mb-4">
                    <label for="namaPromosi" class="form-label">Nama Promosi</label>
                    <input type="text" id="namaPromosi" class="form-control" placeholder="${namaPromo}">
                </div>
            </fieldset>
            <div class="form-outline mb-4">
                <label class="form-label">Diskon (dalam %)</label>
                <input id="diskon-transaksi" class="form-control" type="number" name="nama"></input>
            </div>
            <div class="form-outline mb-4">
                <label class="form-label">Minimum Transaksi</label>
                <input id="mintransaksi-baru" class="form-control" type="number" name="nama"></input>
            </div>
        `);

        $('#ubahModalFooter').html(`                
        <button type="button" class="btn btn-outline-success" data-bs-dismiss="modal" onclick="ubahPromoMinTransaksi('${editId}')">Simpan</button>
        `);
    }
}

function ubahPromoHariSpesial(editId) {
    let diskonBaru = $("#diskon-hari").val();
    document.querySelector('#form-ubah-promo').reset();
    $.ajax({
        type: "POST",
        url: `daftar-promo/ubah-promo-hari-spesial/${editId}`,
        data: {
            'diskon': diskonBaru
        }
    });
}

function ubahPromoMinTransaksi(editId) {
    let diskonBaru = $("#diskon-transaksi").val();
    let minTransaksiBaru = $("#mintransaksi-baru").val();
    document.querySelector('#form-ubah-promo').reset();
    $.ajax({
        type: "POST",
        url: `daftar-promo/ubah-promo-transaksi-minimum/${editId}`,
        data: {
            'diskon': diskonBaru,
            'transaksi': minTransaksiBaru
        }
    });
}

// Hapus data di server dan tampilan pengguna
function hapus(idHapus) {
    $.ajax({
        url: `daftar-promo/delete/${idHapus}`,
        success: function () {
            $(`#${idHapus}`).remove()
        }
    });
}