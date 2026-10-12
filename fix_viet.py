
import re

pages = {}

# ============================================================
# KE-TOAN.HTML
# ============================================================
pages['ke-toan.html'] = {
    # title
    '<title>KimQ AI · Ke toan</title>': '<title>KimQ AI · Kế toán</title>',
    '<title>KimQ · Ke Toan</title>': '<title>KimQ AI · Kế toán</title>',
    # hero
    'AI agent cho doi ke toan': 'AI agent cho đội kế toán',
    'khop so, doi soat, khong bo sot': 'khớp số, đối soát, không bỏ sót',
    'Agent tu dong doi chieu so ke ngan hang': 'Agent tự động đối chiếu sao kê ngân hàng',
    'Agent tu dong doi chieu': 'Agent tự động đối chiếu',
    'khop cong no, ghi nhat ky': 'khớp công nợ, ghi nhật ký',
    'giao dich tu khop': 'giao dịch tự khớp',
    'khoan treo bao cao': 'khoản treo báo cáo',
    'sang bat dau doi soat': 'sáng bắt đầu đối soát',
    'lan quen deadline': 'lần quên deadline',
    # flowbox
    'Agent ket noi sao ke ngan hang dem qua': 'Agent kết nối sao kê ngân hàng đêm qua',
    'Agent khop tung giao dich': 'Agent khớp từng giao dịch',
    'giao dich khop tu dong, ghi nhat ky': 'giao dịch khớp tự động, ghi nhật ký',
    'khoan khong khop: agent phan loai': 'khoản không khớp: agent phân loại',
    'Ke toan nhan danh sach khoan treo': 'Kế toán nhận danh sách khoản treo',
    'khoan treo chuyen len ke toan truong': 'khoản treo chuyển lên kế toán trưởng',
    # cards
    'Xu ly hoa don va cong no': 'Xử lý hóa đơn và công nợ',
    'Doi soat ngan hang hang ngay': 'Đối soát ngân hàng hằng ngày',
    'Bao cao hoan tat truoc': 'Báo cáo hoàn tất trước',
    'Khong can nhan su vao som': 'Không cần nhân sự vào sớm',
    # table
    'Thanh toan nha cung cap': 'Thanh toán nhà cung cấp',
    'Khop tu dong': 'Khớp tự động',
    'Hoan tien khach hang': 'Hoàn tiền khách hàng',
    'Phi ngan hang': 'Phí ngân hàng',
    'Phan loai tu dong': 'Phân loại tự động',
    'Giao dich chua co hoa don': 'Giao dịch chưa có hóa đơn',
    'Can xac nhan': 'Cần xác nhận',
    'Giao dich trung so tien': 'Giao dịch trùng số tiền',
    'Chuyen ke toan truong': 'Chuyển kế toán trưởng',
    # brief
    'Ban tin ke toan': 'Bản tin kế toán',
    'Chi phi van hanh': 'Chi phí vận hành',
    'Cong no qua han': 'Công nợ quá hạn',
    'Giao dich khop': 'Giao dịch khớp',
    'Khoan treo': 'Khoản treo',
    'Phat hanh lai hoa don': 'Phát hành lại hóa đơn',
    'Phe duyet phi luu bai': 'Phê duyệt phí lưu bãi',
    'Xac nhan chuyen khoan': 'Xác nhận chuyển khoản',
    # sections
    'Quy trinh xu ly hang ngay': 'Quy trình xử lý hằng ngày',
    'Phan loai giao dich': 'Phân loại giao dịch',
    'Su dung AI trong ke toan': 'Sử dụng AI trong kế toán',
    # cta
    'Xem AI agent ke toan chay that': 'Xem AI agent kế toán chạy thật',
    'Dat lich trao doi': 'Đặt lịch trao đổi',
    'Lien he tu van': 'Liên hệ tư vấn',
    # footer
    'San pham': 'Sản phẩm',
    'Ung dung': 'Ứng dụng',
    'Cong ty': 'Công ty',
    'Ve KimQ': 'Về KimQ',
    'Lo trinh': 'Lộ trình',
    'Lien he': 'Liên hệ',
    # nav
    'Ve KimQ': 'Về KimQ',
    'San pham AI': 'Sản phẩm AI',
    'Lo trinh': 'Lộ trình',
}

print('Script loaded')
