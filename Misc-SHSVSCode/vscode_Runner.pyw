a
    m{�`	  �                   @   s�   d dl Zd dlZ d dl mZ d dl mZ d dlmZ d dlZd dl	Z	d dl
Z
d dlZd dlZd dlZd dlZd dlZ
d dlZG dd� dej�ZG dd� dej�Ze� Ze��  dS )	�    N)�scrolledtext)�ttk)�askopenfilenamec                   @   s   e Zd Zdd� ZdS )�dividerc                 O   s   t jj| g|�R i |�� d S )N)�tk�Frame�__init__)�self�args�kwargs� r   �$E:\Files\School Drive\vscode Run.pywr   
   s    zdivider.__init__N)�__name__�
__module__�__qualname__r   r   r   r   r   r   	   s   r   c                   @   s,   e Zd Zdd� Zdd� Zdd� Zdd� Zd	S )
�mainc                 O   sz   t jj| g|�R i |�� tj�d�| _| �d� | ��  t	�
d� | �dd� d| _| �d| j� t�� | _| ��  d S )Nz!%appdata%\Code\User\settings.json�
SHS VSCode�   FZWM_DELETE_WINDOW)r   �Tkr   �os�path�
expandvars�settings_location�title�powershellInstall�time�sleepZ	resizableZ	completedZprotocol�powershellRemove�getpassZgetuserZusername�widgets)r	   r
   Zkargsr   r   r   r      s    


zmain.__init__c                 C   s�   t j| ddd�}t j| ddd�}t j| ddd�}t j| dd	d�}|��  |��  t| d
ddd�jddd� |��  t| d
ddd�jddd� |��  d S )Nr   )�TkDefaultFont�   Zbold)�textZfontz1A tool to support the running of vscode execution)r    �   �italiczPKeep this window active for VSCode to work
Closing this will close vscode aswell)r    �   u   A ǝǝl uɐp creation)r    �   r$   Zblack�   i^  )ZbgZheight�width�
   )Z
columnspanZpady)r   ZLabelZgridr   )r	   ZlTitleZlDesc1ZlDesc2ZlCreditsr   r   r   r      s    zmain.widgetsc                 C   s�   t �dg� t �dtj�t�� d�dg� t| jd��d}t	�
|�}d|d< d|d	< d|d
< d|d< d|d< |�d� t	j||dd� |��  W d   � n1 s�0    Y  d S )NzZC:\Windows\System32\config\systemprofile\AppData\Local\Programs\Microsoft VS Code\Code.exeZCOPY�9C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exezC:\Program Files\Python38�r+�(C:\Program Files\Python38\powershell.exe�terminal.external.windowsExecZexternal�terminal.explorerKind�terminal.integrated.cwd�python.testing.cwd�!terminal.integrated.shell.windowsr   �   ��indent)�
subprocessZcall�	getoutputr   r   �join�getcwd�openr   �json�load�seek�dump�truncate�r	   �f�datar   r   r   r   '   s    

zmain.powershellInstallc                 C   s�   t �g d�� t �ddg� t| jd��d}t�|�}d|d< d|d< d|d	< d|d
< d|d< |�d� tj||dd� |��  W d   � n1 s�0    Y  | �	�  d S )N)Ztaskkillz/fz/imzCode.exe�delr,   r+   r*   r-   Zfalser.   r/   r0   r1   r   r2   r3   )
r5   r6   r9   r   r:   r;   r<   r=   r>   Zdestroyr?   r   r   r   r   7   s    

&zmain.powershellRemoveN)r   r   r   r   r   r   r   r   r   r   r   r      s   r   )Ztkinterr   Ztkinter.messageboxr   r   Ztkinter.filedialogr   Zurllib.requestZurllibr5   r   Z
webbrowserr:   Z	threadingr   Zos.pathr   r   r   r   r   �mZmainloopr   r   r   r   �<module>   s   0: