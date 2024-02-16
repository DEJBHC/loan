import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, Text, Scrollbar


def equal_principal_and_interest(principal, interest, time):
    monthly_payment = principal * ((interest / 12) * (1 + (interest / 12)) ** time) / (
                ((1 + (interest / 12)) ** time) - 1)
    return ['每月应还 {:.2f}'.format(monthly_payment), '本息合计 {:.2f}'.format(monthly_payment * time),
            '利息 {:.2f}'.format(monthly_payment * time - principal)]


def equal_principal(principal, interest, time):
    principal_and_interest = 0
    monthly_payment_result = ''
    for i in range(int(time) + 1):
        if i == 0:
            continue
        monthly_payment = (principal / time) + (principal - (i - 1) * (principal / time)) * (interest / 12)
        monthly_payment_result += '第' + str(i) + '月应还{:.2f}'.format(monthly_payment) + '\n'
        principal_and_interest += monthly_payment
    return [monthly_payment_result, '本息合计{:.2f}'.format(principal_and_interest),
            '利息{:.2f}'.format(principal_and_interest - principal)]


def monthly_interest_calculation_and_principal_repayment_at_maturity(principal, interest, time):
    monthly_payment = principal * (interest / 12)
    return ['月供(前' + str(time - 1) + '月){:.2f}'.format(monthly_payment),
            '月供(最后 1 月){:.2f}'.format(monthly_payment + principal), '利息{:.2f}'.format(monthly_payment * time),
            '本息合计{:.2f}'.format(principal + monthly_payment * time)]


def quarter_interest_calculation_and_principal_repayment_at_maturity(principal, interest, time):
    monthly_payment = principal * (interest / 4)
    return ['月供(前' + str(time / 12 - 1) + '年至最后 1 年的前 3 季){:.2f}'.format(monthly_payment),
            '月供(最后 1 季){:.2f}'.format(monthly_payment + principal),
            '利息{:.2f}'.format(monthly_payment * (time / 3)),
            '本息合计{:.2f}'.format(principal + monthly_payment * (time / 3))]


def half_year_interest_calculation_and_principal_repayment_at_maturity(principal, interest, time):
    monthly_payment = principal * (interest / 2)
    return ['月供(前' + str(time / 12 - 1) + '年至最后 1 年的上半年){:.2f}'.format(monthly_payment),
            '月供(最后半年){:.2f}'.format(monthly_payment + principal),
            '利息{:.2f}'.format(monthly_payment * (time / 6)),
            '本息合计{:.2f}'.format(principal + monthly_payment * (time / 6))]


def year_interest_calculation_and_principal_repayment_at_maturity(principal, interest, time):
    monthly_payment = principal * (interest)
    return ['月供(前' + str(time / 12 - 1) + '年){:.2f}'.format(monthly_payment),
            '月供(最后 1 年){:.2f}'.format(monthly_payment + principal),
            '利息{:.2f}'.format(monthly_payment * (time / 12)),
            '本息合计{:.2f}'.format(principal + monthly_payment * (time / 12))]


def one_time_interest_calculation_and_principal_repayment_at_maturity(principal, interest, time):
    monthly_payment = principal * (interest)
    return ['利息{:.2f}'.format(monthly_payment * (time / 12)),
            '本息合计{:.2f}'.format(principal + monthly_payment * (time / 12))]


def main_window():
    def custom_message_box(title, message, parent=None):
        # 创建一个自定义对话框
        dialog = tk.Toplevel(parent)
        dialog.title(title)
        dialog.geometry('+%d+%d' % (parent.winfo_rootx() + 50, parent.winfo_rooty() + 50))

        # 创建一个Text控件用于显示消息
        text_widget = Text(dialog, wrap=tk.WORD, width=60, height=20)
        text_widget.insert(tk.END, message)
        text_widget.config(state='disabled')  # 设置为只读

        # 创建一个垂直滚动条
        scrollbar = Scrollbar(dialog, command=text_widget.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # 将Text控件和滚动条添加到对话框中
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=text_widget.yview)

        # 显示对话框
        dialog.wait_window()

    def on_button_click():
        # 假设我们想要将三个输入框的内容以及下拉框的选择打印到只读文本框中
        principal = float(principal_entry.get())
        interest_rate = float(interest_rate_entry.get())
        time = float(time_entry.get())
        selection = combo_box.get()
        if selection == '等额本息':
            result = equal_principal_and_interest(principal, interest_rate, time)
            messagebox.showinfo('等额本息', result[0] + '\n' + result[1] + '\n' + result[2])
        elif selection == '等额本金':
            result = equal_principal(principal, interest_rate, time)
            custom_message_box('等额本金', result[0] + '\n' + result[1] + '\n' + result[2], parent=root)
        elif selection == '按月付息，到期还本':
            result = monthly_interest_calculation_and_principal_repayment_at_maturity(principal, interest_rate, time)
            for i in result:
                print(i)
            messagebox.showinfo('按月付息，到期还本', result[0] + '\n' + result[1] + '\n' + result[2] + '\n' + result[3])
        elif selection == '按季付息，到期还本':
            result = quarter_interest_calculation_and_principal_repayment_at_maturity(principal, interest_rate, time)
            messagebox.showinfo('按季付息，到期还本', result[0] + '\n' + result[1] + '\n' + result[2] + '\n' + result[3])
        elif selection == '按半年付息，到期还本':
            result = half_year_interest_calculation_and_principal_repayment_at_maturity(principal, interest_rate, time)
            messagebox.showinfo('按半年付息，到期还本',
                                result[0] + '\n' + result[1] + '\n' + result[2] + '\n' + result[3])
        elif selection == '按年付息，到期还本':
            result = year_interest_calculation_and_principal_repayment_at_maturity(principal, interest_rate, time)
            messagebox.showinfo('按年付息，到期还本', result[0] + '\n' + result[1] + '\n' + result[2] + '\n' + result[3])
        elif selection == '一次性利随本清':
            result = one_time_interest_calculation_and_principal_repayment_at_maturity(principal, interest_rate, time)
            messagebox.showinfo('一次性利随本清', result[0] + '\n' + result[1])

    # 创建主窗口
    root = tk.Tk()
    root.geometry("300x250")
    root.title("贷款计算器")

    # 创建金额输入框
    principal_label = tk.Label(root, text="贷款金额(单位/元)")
    principal_label.pack(side=tk.TOP, pady=10)
    principal_entry = tk.Entry(root)
    principal_entry.insert(0, '200000')
    principal_entry.pack()

    # 创建利率输入框
    interest_rate_label = tk.Label(root, text="年利率")
    interest_rate_label.pack()
    interest_rate_entry = tk.Entry(root)
    interest_rate_entry.insert(0, '0.04')
    interest_rate_entry.pack()

    # 创建时间输入框
    time_label = tk.Label(root, text="贷款时间(单位：月)")
    time_label.pack()
    time_entry = tk.Entry(root)
    time_entry.insert(0, '240')
    time_entry.pack()

    # 创建下拉选择框
    combo_box_label = tk.Label(root, text="还款方式")
    combo_box_label.pack()
    combo_box = ttk.Combobox(root, values=["等额本息", "等额本金", "按月付息，到期还本", "按季付息，到期还本",
                                           "按半年付息，到期还本", "按年付息，到期还本", "一次性利随本清"],
                             state='readonly')
    combo_box.set('等额本息')
    combo_box.pack()

    # 创建确定按钮
    button = tk.Button(root, text="计算", command=on_button_click)
    button.pack()

    # 运行主循环
    root.mainloop()


if __name__ == '__main__':
    main_window()
