import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng Dụng Xử Lý Ảnh")

        # Khởi tạo biến lưu ảnh
        self.original_image = None
        self.processed_image = None

        # Giao diện người dùng
        self.setup_ui()

    def setup_ui(self):
        # Tạo các nút và gắn các sự kiện
        self.load_button = tk.Button(self.root, text="Tải Ảnh", command=self.load_image)
        self.load_button.pack(side=tk.TOP, padx=10, pady=10)

        self.equalize_button = tk.Button(self.root, text="Cân Bằng Mức Xám", command=self.equalize_image)
        self.equalize_button.pack(side=tk.TOP, padx=10, pady=10)

        self.histogram_button = tk.Button(self.root, text="Hiển Thị Histogram", command=self.show_histogram)
        self.histogram_button.pack(side=tk.TOP, padx=10, pady=10)

        # Hiển thị ảnh gốc và sau khi cân bằng
        self.image_label_original = tk.Label(self.root)
        self.image_label_original.pack(padx=10, pady=10, side=tk.TOP)

        self.image_label_processed = tk.Label(self.root)
        self.image_label_processed.pack(padx=10, pady=10, side=tk.TOP)

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.original_image = cv2.imread(file_path)
            self.display_image(self.original_image, self.image_label_original)
            self.processed_image = None  # Đặt lại ảnh đã xử lý khi tải ảnh mới

    def equalize_image(self):
        if self.original_image is not None:
            gray_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
            equalized_image = cv2.equalizeHist(gray_image)
            self.display_image(equalized_image, self.image_label_processed)
            self.processed_image = equalized_image

    def show_histogram(self):
        if self.original_image is not None and self.processed_image is not None:
            # HISTOGRAM ẢNH GỐC
            gray_original = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
            hist_original = cv2.calcHist([gray_original], [0], None, [256], [0, 256])

            # HISTOGRAM ẢNH CÂN BẰNG
            hist_equalized = cv2.calcHist([self.processed_image], [0], None, [256], [0, 256])

            # Tạo biểu đồ histogram cho ảnh gốc
            fig_original, ax_original = plt.subplots()
            ax_original.plot(hist_original, label='Ảnh Gốc')
            ax_original.set_title('Histogram ảnh gốc')
            ax_original.set_xlabel('Mức Xám')
            ax_original.set_ylabel('Số Lượng Pixel')
            ax_original.legend()

            # Tạo cửa sổ mới để hiển thị biểu đồ histogram ảnh gốc
            histogram_window_original = tk.Toplevel(self.root)
            histogram_window_original.title("Biểu Đồ Histogram Ảnh Gốc")

            canvas_original = FigureCanvasTkAgg(fig_original, master=histogram_window_original)
            canvas_original.draw()
            canvas_original.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            toolbar_original = NavigationToolbar2Tk(canvas_original, histogram_window_original)
            toolbar_original.update()
            canvas_original.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            # Tạo biểu đồ histogram cho ảnh cân bằng
            fig_equalized, ax_equalized = plt.subplots()
            ax_equalized.plot(hist_equalized, label='Ảnh Cân Bằng')
            ax_equalized.set_title('Histogram ảnh cân bằng')
            ax_equalized.set_xlabel('Mức Xám')
            ax_equalized.set_ylabel('Số Lượng Pixel')
            ax_equalized.legend()

            # Tạo cửa sổ mới để hiển thị biểu đồ histogram ảnh cân bằng
            histogram_window_equalized = tk.Toplevel(self.root)
            histogram_window_equalized.title("Biểu Đồ Histogram Ảnh Cân Bằng")

            canvas_equalized = FigureCanvasTkAgg(fig_equalized, master=histogram_window_equalized)
            canvas_equalized.draw()
            canvas_equalized.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            toolbar_equalized = NavigationToolbar2Tk(canvas_equalized, histogram_window_equalized)
            toolbar_equalized.update()
            canvas_equalized.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def display_image(self, image, label):
        # Chuyển đổi ảnh sang định dạng phù hợp để hiển thị trong Tkinter
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Giảm kích thước ảnh để hiển thị nhỏ hơn
        max_width = 300
        height, width, _ = image.shape
        ratio = max_width / width
        resized_image = cv2.resize(image, (int(width * ratio), int(height * ratio)))

        pil_image = Image.fromarray(resized_image)
        tk_image = ImageTk.PhotoImage(image=pil_image)

        # Cập nhật ảnh trên label
        label.configure(image=tk_image)
        label.image = tk_image

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()
