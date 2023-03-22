import tkinter as tk
from tkinter import messagebox
import solver
from Puzzle_Generator import generate
import sys
import time
import random

FONT = ('Times New Roman', 30)
colourIndex = 0
flashColours = [
    'snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'thistle', 'snow2', 'snow3',
    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4'
    ]
def playAgain(rootWindow):

    reply = messagebox.askyesno('Play again?', 'Do you wish to play again?')

    if reply:
        messagebox.showinfo('Sudoku', 'Generating puzzle..')
        rootWindow.destroy()
        main()
        
    else:
        messagebox.showinfo('Sudoku', 'Thanks for playing!')
        rootWindow.destroy()
        sys.exit()


strikeNo = 0      

def main():

    global strikeNo
    window = tk.Tk()
    window.geometry('700x825+400+0')
    WINDOW_BG = 'royal blue'
    window.configure(bg=WINDOW_BG)
    window.title('Sudoku Solver!')
    
    def exitProgram(event=None):
        if tk.messagebox.askyesno('Exit', 'Do you wish to quit?'):
            window.destroy()
            sys.exit()
    window.protocol('WM_DELETE_WINDOW', exitProgram)

    window.focus_force()

    board, SolvedBoard = generate() #Returns the puzzle and it's solved state

    highlightFrames = []

    SudokuBoard = tk.Frame(window, bg='white', pady=5)

    FRAME_BG = 'gold'
    statusBar = tk.Frame(window, bg=FRAME_BG, pady=5)


    tk.Label(window, bg=WINDOW_BG, pady=2).pack()

    strikesFrame = tk.Frame(statusBar, bg=FRAME_BG)
    tk.Label(strikesFrame, text='Strikes:', fg='green', bg=FRAME_BG, font=FONT).grid(row=0, column=0)
    strikes = tk.Label(strikesFrame, fg = 'brown', bg=FRAME_BG, font = FONT)
    strikes.grid(row = 0, column = 1)
    strikeNo = 0

    brokenRunFrame = tk.Frame(statusBar, bg =FRAME_BG, padx = 5)
    brokenRun = tk.Label(brokenRunFrame, bg=FRAME_BG, font=('Verdana', 10), text='BROKEN RUN!', fg='red')
    brokenRun.pack()

    def updateTime():
        global afterId
        minute, second = [int(i) for i in timeLabel['text'].split(':')]
        second += 1
        if second == 60:
            minute += 1
            second = 0

        timeLabel['text'] = str(minute).zfill(2) + ':' + str(second).zfill(2)
        afterId = timeLabel.after(1000, updateTime)

    timeFrame = tk.Frame(statusBar, bg=FRAME_BG)
    tk.Label(timeFrame, text='Time: ', fg='green', bg=FRAME_BG, font=FONT).grid(row=0, column=0)
    timeLabel = tk.Label(timeFrame, text='00:00', bg=FRAME_BG, fg='red', font=FONT, padx=5)
    timeLabel.grid(row=0, column=1)

    def highlightColour(borderFrame, colour, label=tk.Label(), posTup=None):
        if colour in ['lime', 'white']:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j]['text'] == label['text']:
                        highlightFrames[i][j]['bg'] = colour
                        
        else:
            borderFrame['bg'] = colour
            
        if label['fg'] != 'blue':
            #window.bind('<ButtonPress>', lambda event, label=label: makeGuesses(label, '1'))
            window.bind('<Key>', lambda event, child=label, pos=posTup: update(child, event.char, pos))
            
##    def makeGuesses(label, num):
##        label['font'] = ('Times New Roman', 10)
##        label['text'] += num

    def update(label, num, pos):

        global strikeNo

        if label['text'] != '' or not all([num in[str(i) for i in range(1, len(board) + 1)], pos]):

            return

        previousText = label['text']
        label['text'] = int(num)

        if SolvedBoard[pos[0]][pos[1]] != int(num):

            strikeNo += 1

            messagebox.showerror('Invalid!', 'Strike %d!' % strikeNo)

            strikes['text'] = 'X' * strikeNo

            label['text'] = previousText

            if strikeNo > 3:

                strikes['fg'] = 'red'

                brokenRunFrame.pack(before=timeFrame)

        elif SolvedBoard == BoardStatus(board):

            #Displaying game stats, and requesting play again
            win_msg = '''Congratulations! You win!
Strikes: %s
Time taken: %s
''' % (strikeNo, timeLabel['text'])

            messagebox.showinfo('Game Over!', win_msg)

            playAgain(window)

    x = y = 0

    def getColour(label):
        if label['text']:
            return 'lime'
        return 'red'

    for i in range(len(board)):

        highlightFrames.append([])

        if i % 3 == 0 and i != 0:

            for k in range(12):

                if k % 4 != 0:

                    l = tk.Label(SudokuBoard, font = ('Times New Roman', 1),
                                 bg = 'black', width = 45, padx = 1)

                    l.grid(row = y, column = k)


            y += 1

        for j in range(len(board[i])):

            frame = tk.Frame(SudokuBoard, bg='white', padx=2, pady=2)

            if board[i][j] == 0:

                value = ''

                board[i][j] = tk.Label(frame, font = FONT, width = 2, bg = 'white',
                                       text = '', relief = tk.SUNKEN)

            else:

                value = board[i][j]

                board[i][j] = tk.Label(frame, font = FONT, width = 2, bg = 'white',
                                       fg = 'blue', text = value, relief = tk.SUNKEN)

            board[i][j].pack()

            board[i][j].bind('<Enter>',
                             lambda event, ele=frame, label=board[i][j],
                             pos=(i, j): highlightColour(ele, getColour(label), label, pos))
            board[i][j].bind('<Leave>', lambda event, ele=frame, label=board[i][j],
                             pos=(i, j): highlightColour(ele, 'white', label))
                
            if j % 3 == 0:

                l = tk.Label(SudokuBoard, text = '', bg = 'black', font = FONT, padx = 1)

                if j == 0: l['bg'] = 'white'

                l.grid(row = y, column = x)

                x += 1
                

            frame.grid(row = y, column = x)

            highlightFrames[i].append(frame)

            x += 1

        x = 0

        y += 1

    tk.Label(window, text='Sudoku!', bg='orange', fg='red', padx=20, pady=10,
             font=('Verdana', 30)).pack()

    tk.Label(window, bg=WINDOW_BG, pady=5).pack()


    SudokuBoard.pack()

    updateTime() #Start time updation after the board is packed to window

    strikesFrame.pack()
    timeFrame.pack()

    statusBar.pack(pady=20)

    def BoardStatus(Board):
        return [[int(label['text']) if label['text']!= '' else 0 for label in row] for row in Board]
    
    def solveSudokuPuzzle(LabelBoard=board):
        Board = BoardStatus(LabelBoard)
        found = solver.findEmpty(Board)
        if not found:
            messagebox.showinfo('Solution found!', 'Puzzle solved!')
            return True
        
        row, col = found
        
        for i in range(1, len(Board) + 1):

            LabelBoard[row][col]['text'] = i

            highlightFrames[row][col]['bg'] = 'red'

            if solver.isValid(Board, val = i, pos = (row, col)):

                Board[row][col] = i

                LabelBoard[row][col]['text'] = i

                highlightFrames[row][col]['bg'] = 'lime'
                try:
                    solved = solveSudokuPuzzle(LabelBoard)
                except Exception:
                    print('\n** Solve terminated! **')
                    sys.exit()
                if solved:
                    playAgain(window)

                highlightFrames[row][col]['bg'] = 'red'

                Board[row][col] = 0

                LabelBoard[row][col]['text'] = ''

            else:

                LabelBoard[row][col]['text'] = ''

            window.update()

            time.sleep(0.025)


        return False
    
    def solvingPreparations(event):
        for i, row in enumerate(board):
            for j, label in enumerate(row):
                label.unbind('<Enter>')
                label.unbind('<Leave>')
                highlightFrames[i][j]['bg'] = 'white'
        timeLabel.after_cancel(afterId)
        window.unbind('<Double-1>')
        solveSudokuPuzzle(board)

    def exitProgram(event=None):
        if tk.messagebox.askyesno('Exit', 'Do you wish to quit?'):
            window.destroy()
            menuScreen()
    window.protocol('WM_DELETE_WINDOW', exitProgram)
    window.bind('<Double-1>', solvingPreparations)
    window.mainloop()

def solverScreen():
    window = tk.Tk()
    window.geometry('700x750+400+0')
    window.configure(bg='aqua')
    window.title('Sudoku Solver!')
    highlightFrames = []
    SudokuBoard = tk.Frame(window, bg='white')
    window.focus_force()

    tk.Label(window, text = 'Sudoku!', bg = 'orange', fg = 'red', padx = 20, pady = 10,
             font = ('Verdana', 30)).pack(pady=10)

    def clearLabel(label):
        label['text'] = ''
    def update(label, num, pos):
        if num.isdigit() and int(num) != 0:
            label['fg'] = 'blue'
            label['text'] = int(num)
        elif num == 'c':
            clearLabel(label)
    
    def highlightColour(borderFrame, colour, label=tk.Label(), posTup=None):
        borderFrame['bg'] = colour
        window.bind('<Key>', lambda event, child=label, pos=posTup: update(child, event.char, pos))
        window.bind('<Button>', lambda event, label=label: clearLabel(label))
        
    FONT = ('Times New Roman', 30)

    def solvingPreparations(event=None):
        global reset
        reset = False
        for i, row in enumerate(board):
            for j, label in enumerate(row):
                label.unbind('<Enter>')
                label.unbind('<Leave>')
                highlightFrames[i][j]['bg'] = 'white'
        window.unbind('<Double-1>')
        solveBtn['state'] = 'disabled'
        solveSudokuPuzzle(board)
        
    def resetBoard(event=None):
        global reset
        reset = True
        for i, row in enumerate(board):
            for j, label in enumerate(row):
                label['text'] = ''
                highlightFrames[i][j]['bg'] = 'white'
        solveBtn['state'] = 'normal'
        highlightFrames.clear()
        initializeBoard(SudokuBoard)
        
    buttonsFrame = tk.Frame(window, bg='aqua', pady=10)
    BUTTON_BG = 'gold'
    BUTTON_FG = 'red'
    
    buttonsFrame.columnconfigure(0, weight=1)
    buttonsFrame.columnconfigure(1, weight=1)
    solveBtn = tk.Button(buttonsFrame, text='Solve board', font=('Verdana', 20),
                         command=solvingPreparations, bg=BUTTON_BG, fg=BUTTON_FG,
                         activeforeground='red', activebackground='gold',
                         disabledforeground=BUTTON_FG)
    resetBtn = tk.Button(buttonsFrame, text='Reset board', font=('Verdana', 20),
                         command=resetBoard, bg=BUTTON_BG, fg=BUTTON_FG,
                         activeforeground='red', activebackground='gold')
    solveBtn.grid(row=0, column=0, sticky='ne', padx=20)
    resetBtn.grid(row=0, column=1, sticky='nw')
    buttonsFrame.pack(fill='both')
    
    def initializeBoard(SudokuBoard):
        global board
        SudokuBoard.destroy()
        SudokuBoard = tk.Frame(window, bg = 'white', pady = 5)
        x = y = 0
        board = [[0 for j in range(9)] for i in range(9)]
        for i in range(len(board)):
            highlightFrames.append([])
            if i % 3 == 0 and i != 0:
                for k in range(12):
                    if k % 4 != 0:
                        l = tk.Label(SudokuBoard, font = ('Times New Roman', 1),
                                     bg = 'black', width = 45, padx = 1)
                        l.grid(row = y, column = k)
                y += 1
            for j in range(len(board[i])):
                frame = tk.Frame(SudokuBoard, bg='white', padx=2, pady=2)
                if board[i][j] == 0:
                    value = ''
                    board[i][j] = tk.Label(frame, font = FONT, width = 2, bg = 'white',
                                           text = '', relief = tk.SUNKEN)
                else:
                    value = board[i][j]
                    board[i][j] = tk.Label(frame, font = FONT, width = 2, bg = 'white',
                                           fg = 'blue', text = value, relief = tk.SUNKEN)
                board[i][j].pack()
                board[i][j].bind('<Enter>',
                                 lambda event, ele=frame, label=board[i][j],
                                 pos=(i, j): highlightColour(ele, 'red', label, pos))
                board[i][j].bind('<Leave>', lambda event, ele=frame, label=board[i][j],
                                 pos=(i, j): highlightColour(ele, 'white'))
                if j % 3 == 0:
                    l = tk.Label(SudokuBoard, text = '', bg = 'black', font = FONT, padx = 1)
                    if j == 0: l['bg'] = 'white'
                    l.grid(row = y, column = x)
                    x += 1
                frame.grid(row = y, column = x)
                highlightFrames[i].append(frame)
                x += 1
            x = 0
            y += 1
        SudokuBoard.pack(before=buttonsFrame, pady=10)
        return SudokuBoard
    
    SudokuBoard = initializeBoard(SudokuBoard)

    def BoardStatus(Board):
        return [[int(label['text']) if label['text']!= '' else 0 for label in row] for row in Board]
    
    def solveSudokuPuzzle(LabelBoard=board):
        Board = BoardStatus(LabelBoard)
        found = solver.findEmpty(Board)
        if not found:
            messagebox.showinfo('Solution found!', 'Puzzle solved!')
            return True
        
        row, col = found
        
        for i in range(1, len(Board) + 1):
            LabelBoard[row][col]['text'] = i
            highlightFrames[row][col]['bg'] = 'red'
            if solver.isValid(Board, val = i, pos = (row, col)):
                Board[row][col] = i
                LabelBoard[row][col]['text'] = i
                highlightFrames[row][col]['bg'] = 'lime'
                try:
                    solved = solveSudokuPuzzle(LabelBoard)
                except Exception:
                    print('\n** Solve terminated! **')
                    messagebox.showinfo('Solve terminated', 'Solve has been terminated!')
                    menuScreen()
                if solved or reset:
                    return
                highlightFrames[row][col]['bg'] = 'red'
                Board[row][col] = 0
                LabelBoard[row][col]['text'] = ''
            else:
                LabelBoard[row][col]['text'] = ''
            window.update()
            time.sleep(0.025)
        return False

    def exitProgram(event=None):
        if tk.messagebox.askyesno('Exit', 'Do you wish to quit?'):
            window.destroy()
            menuScreen()
    window.protocol('WM_DELETE_WINDOW', exitProgram)
    window.bind('<Double-1>', solvingPreparations)
    window.bind('<Return>', resetBoard)
    window.mainloop()

menuBoard = generate(logs=False)[0]
def menuScreen():
    window = tk.Tk()
    window.geometry('700x825+400+0')
    window.configure(bg='green3')
    window.title('Sudoku Solver!')
    window.option_add('*Button.foreground', 'red')
    window.option_add('*Button.background', 'gold')
    tk.Label(window, text= 'Sudoku!', bg='orange', fg='red', padx=20, pady=10, font=('Verdana', 30)).pack()
    boardHighlightFrame = tk.Frame(window, bg='red', padx=10, pady=10)
    boardHighlightFrame.pack(pady=20)
    
    def initializeBoard():
        SudokuBoard = tk.Frame(boardHighlightFrame, bg='white', pady=5)
        x = y = 0
        for i in range(len(menuBoard)):
            if i % 3 == 0 and i != 0:
                for k in range(12):
                    if k % 4 != 0:
                        l = tk.Label(SudokuBoard, font = ('Times New Roman', 1),
                                     bg = 'black', width = 45, padx = 1)
                        l.grid(row = y, column = k)
                y += 1
            for j in range(len(menuBoard[i])):
                frame = tk.Frame(SudokuBoard, bg='white', padx=2, pady=2)
                label = tk.Label(frame, font=FONT, width=2, bg='white', fg='blue',
                                 text=menuBoard[i][j] if menuBoard[i][j] else '',
                                 relief=tk.SUNKEN)
                label.pack()
                if j % 3 == 0:
                    l = tk.Label(SudokuBoard, text='', bg='black', font=FONT, padx=1)
                    if j == 0: l['bg'] = 'white'
                    l.grid(row = y, column = x)
                    x += 1
                frame.grid(row = y, column = x)
                x += 1
            x = 0
            y += 1
        SudokuBoard.pack()
            
    initializeBoard()
    buttonsFrame = tk.Frame(window, bg='aqua', padx=10, pady=10)
    buttonsFrame.columnconfigure(0, weight=1)
    buttonsFrame.columnconfigure(1, weight=1)
    
    def initializeSolver():
        if not complete:
            messagebox.showinfo('Coming soon', 'Coming soon!')
        else:
            window.destroy()
            solverScreen()
    solver = tk.Button(buttonsFrame, text='Solver', font=('Verdana', 30),
                       activeforeground='red', activebackground='gold',
                       command=initializeSolver, padx=5)
    solver.grid(row=0, column=0, sticky='nsew')
    play = tk.Button(buttonsFrame, text='Play', font=('Verdana', 30),
                     activeforeground='red', activebackground='gold',
                     command=lambda:(window.destroy(), main()))
    play.grid(row=0, column=1, sticky='nsew')
    play.flash()
    buttonsFrame.pack(fill='x', expand=1)
    complete = True

    def flashBoard():
        global colourIndex
        boardHighlightFrame['bg'] = flashColours[colourIndex]
        colourIndex += 1
        if colourIndex == len(flashColours):
            colourIndex = 0
        boardHighlightFrame.after(100, flashBoard)
    boardHighlightFrame.after(1000, flashBoard)
    
    def exitProgram(event=None):
        if tk.messagebox.askyesno('Exit', 'Do you wish to quit?'):
            window.destroy()
            sys.exit()
    window.protocol('WM_DELETE_WINDOW', exitProgram)

menuScreen()
