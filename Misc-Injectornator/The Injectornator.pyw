U
    �Ty`q1  �                   @   s�   d dl Zd dlZ d dl mZ d dl mZ d dlmZ d dlZd dl	Z	d dl
Z
d dlZd dlZd dlZd dlZd dlZ
G dd� dej�ZG dd� dej�ZG d	d
� d
ej�Ze� Ze��  dS )�    N)�scrolledtext)�ttk)�askopenfilenamec                   @   s   e Zd Zdd� Zdd� ZdS )�
scrollTextc                 O   s   t jj| f|�|� d S �N)r   �ScrolledText�__init__��self�args�kwargs� r   �something.pywr   
   s    zscrollText.__init__c                 C   s8   | j dd� | �dt|�d � | j dd� | ��  d S )NZnormal)�state�end�
�disabled)Zconfig�insert�str�update)r
   �textr   r   r   �
insertText   s    zscrollText.insertTextN)�__name__�
__module__�__qualname__r   r   r   r   r   r   r   	   s   r   c                   @   s   e Zd Zdd� ZdS )�dividerc                 O   s   t jj| f|�|� d S r   )�tk�Framer   r	   r   r   r   r      s    zdivider.__init__N)r   r   r   r   r   r   r   r   r      s   r   c                   @   s|   e Zd Zdd� Zdd� Zdd� Zdd� Zd	d
� Zdd� Zdd� Z	dd� Z
dd� Zdd� Zdd� Zdd� Zdd� Zdd� ZdS )�mainc                 O   sn   t jj| f|�|� | �d� | �dd� d| _d| _t�� | _	| �
�  d| _dddddd	ddd
dd�
| _d S )N�The InjectornatorF�>https://dl.google.com/drive-file-stream/GoogleDriveFSSetup.exez%tmp%zvscode-icons�firstZ!automaticallyOverrodeDefaultValue�(C:\Program Files\Python38\powershell.exeZexternalr   )
zworkbench.iconThemezeditor.suggestSelectionz,vsintellicode.modify.editor.suggestSelectionzpython.jediEnabledzterminal.external.windowsExeczterminal.explorerKindzterminal.integrated.cwdzpython.testing.cwdzwindow.zoomLevelz!terminal.integrated.shell.windows)r   �Tkr   �titleZ	resizable�url�	completed�getpassZgetuserZusername�widgets�location�json_vs_code_powershell)r
   r   Zkargsr   r   r   r      s&    

�zmain.__init__c                    s@  t � tjdddd�� _tj� ddd�� _tj� dd	d�}tj� d
dd�� _tj� d� fdd�d�� _	tj� ddd�� _
t�� �� _tj� d� fdd�d�� _tj� ddd�}tj� ddd�}tj� d� fdd�d�}tj� d� fdd�d�}tj� d� fdd�d�}tj� ddd�}tj� ddd�}tj� d� fd d�d�}	tj� d!� fd"d�d�}
tj� d#� fd$d�d�}tj� d%� fd&d�d�}tj� d'dd�}� jjd(d)d*� |jd+d)d*� t� d,d)d-d.�jd/d)dd0� � jjd)d)d*� � j	jd1d(d)d2� � j
jd3d(d4� � jjd3d+d4� � jjd3d/d4� t� d,d)d-d.�jd5d)dd0� |jd6d)d*� |jd7d)d*� |jd8d(d4� |jd8d+d4� |jd8d/d4� t� d,d)d-d.�jd)dd9� |jd)d:d;� |	jd(d<d=� |
jd+d<d=� |jd/d<d=� |jd+d>d=� t� d,d)d-d.�jd)dd9� |jd)d?� � jjd)d?� t� d,d)d-d.�jd)dd9� |jd)d?� d S )@N�(   �
   r   )Zwrap�width�heightr   r   )�TkDefaultFont�   �bold)r   Zfontz,A helpful tool to add features to SHS Win 10)r/   �   �italicZ	Installer)r/   �   r1   zGoogle Drive Installerc                      s   � � � S r   )�driveInstallerr   �r
   r   r   �<lambda>1   �    zmain.widgets.<locals>.<lambda>)r   ZcommandzCustom Install)r/   r2   ZInstallc                      s   � � � S r   )�customInstallr   r6   r   r   r7   5   r8   Z
Powershellz3Recommended to remove after use to remove detection)r/   �   r3   zLaunch Powershellc                      s   � � � S r   )�powershell_runr   r6   r   r   r7   9   r8   zRemove Powershellc                      s   � � � S r   )�powershellRemover   r6   r   r   r7   :   r8   zVSCode Configc                      s   � � � S r   )�vsCodeInstallr   r6   r   r   r7   ;   r8   zLog:zWindows Tweaksz	Dark Modec                      s
   � � d�S )N�dark��themer   r6   r   r   r7   ?   r8   zDefault Modec                      s
   � � d�S )N�defaultr?   r   r6   r   r   r7   @   r8   Z	Wallpaperc                      s   � � � S r   )�	wallpaperr   r6   r   r   r7   A   r8   zChrome Themec                      s   � � � S r   )�chromer   r6   r   r   r7   B   r8   u   A ǝǝl uɐp creationr   �   )�row�
columnspan�   Zblacki^  )Zbgr.   r-   �   )rE   rF   �pady�   )rE   �columnrF   �   )rE   rK   �   �   r:   �	   )rF   rI   r2   )rF   rE   �   )rK   rE   �   )rF   )r   r   ZWORD�logZLabelZltitleZlinstaller_titler   ZButtonZbgoogledriveZlcustomZEntry�eurl_locZburl_locZgridr   )r
   Zltitle_descZlpowerShellZlpowerShell_descZbpowershellZbpowershell_removeZbvs_code_powershell_configZllogZltweak_titleZ	bdarkModeZbdefaultModeZbCustomWallpaperZbCustomChromeZlCreditsr   r6   r   r(   ,   sZ    zmain.widgetsc              
   C   s&  | j �d� tj�d�r�| j �d� | j �t�dtj�t�� d�dg�� | j �t�dg�� t	j
�dd�r�| j �d	� | j �t�d
dg�� | j �d� n�| j �d� d}z*tj| j|fd�}| j �d� |��  W n6 tk
�r } z| j �d�|�� W 5 d }~X Y nX | j �d� | ��  d S )NzVerifying Installer�GoogleDrive.exe�File Valid
Installing�COPY�C:\Program Files\Python38z)C:\Program Files\Python38\GoogleDrive.exe�Remove Injectionz=Google Drive has been installed. Continue to remove injection�Removing Injection�delzDrive has been installedz%File Invalid
Trying online version...r    ��targetr   �Downloading�	Error: {}�Waiting)rR   r   �os�path�exists�
subprocess�	getoutput�join�getcwdr   �
messagebox�showinfo�	threading�Thread�
downloader�start�	Exception�format�waitForDownload�r
   r%   ZdownloadThread�er   r   r   r5   `   s&    &$zmain.driveInstallerc                 C   s    | � �  | j�t�dg�� d S )Nr"   )�
powershellrR   r   rc   �callr6   r   r   r   r;   x   s    zmain.powershell_runc              	   C   sB   | j �d� | j �t�dtj�t�� d�dg�� | j �d� d S )NzFetching powershellrV   z9C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exerW   z Launching Powershell - check cli)rR   r   rc   rd   r`   ra   re   rf   r6   r   r   r   rr   {   s    &zmain.powershellc                 C   s&   | j �t�ddg�� | j �d� d S )NrZ   r"   zPowershell Removed)rR   r   rc   rd   r6   r   r   r   r<   �   s    zmain.powershellRemovec              	   C   sZ   t j�d�}| j�| j� t|d�� }| j�|�t�	| j��� W 5 Q R X | j�d� d S )Nz!%appdata%\Code\User\settings.json�wZComplete)
r`   ra   �
expandvarsrR   r   r*   �open�write�json�dumps)r
   Zsettings_location�fr   r   r   r=   �   s
    $zmain.vsCodeInstallc              	   C   s�   | j �d� | j �t�d| jdg�� | j �t�tj�d| j�g�� t	j
�dd�r�| j �d� | j �t�dtj�d| j�g�� | j �t�d| jg�� | j �d	� d S )
NrU   rV   rW   zC:\Program Files\Python38\ rX   z8Program has been installed. Continue to remove injectionrY   rZ   zProgram has been installed)rR   r   rc   rd   �fileLocationr`   ra   re   �fileNamer   rg   rh   r6   r   r   r   �install�   s     "zmain.installc              
   C   s�   | j �� }t|� |dd� �� dks:|dd� �� dkr�td� z*tj| j|fd�}| j�d� |�	�  W n4 t
k
r� } z| j�d	�|�� W 5 d }~X Y q�X | j�d
� | ��  n|| _d| _| ��  d S )Nr   rJ   ZhttprD   Zwww�1r[   r]   r^   r_   rT   )rS   �get�print�lowerri   rj   rk   rR   r   rl   rm   rn   ro   r{   r|   r}   rp   r   r   r   r9   �   s    
($
zmain.customInstallc                 C   s4   | j r"d| _ | j�d� | ��  n| �d| j� d S )NFzDownload successful�d   )r&   rR   r   r}   Zafterro   r6   r   r   r   ro   �   s
    
zmain.waitForDownloadc              
   C   sR  |dd � }z8t j�|tj�tj�d�d| �� ttj�d�� W n� t jj	k
r~ } zt|� | j
�d� W 5 d }~X Y n� t jjk
r� } zt|� | j
�d� W 5 d }~X Y n� tk
r� } zt|� | j
�d� W 5 d }~X Y nd tk
�r  } zt|� | j
�d� W 5 d }~X Y n.X d| | _tj�tj�d�d| �| _d| _d S )N�����z%temp%z64616e6c6565.z&File not found. Download unsuccessful.z#URL invalid. Download unsuccessful.z'An error occured. Download unsuccessfulT)�urllibZrequestZurlretriever`   ra   re   ru   r�   �errorZ	HTTPErrorrR   r   ZURLError�
ValueErrorrm   r|   r{   r&   )r
   r%   Zext�arq   r   r   r   rk   �   s&    $
zmain.downloaderc                 C   sZ   | � �  d}d}|dkr0| j�t�d|g�� n|dkrN| j�t�d|g�� | ��  d S )NzzNew-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize -Name AppsUseLightTheme -Value 0ztRemove-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize -Name AppsUseLightThemer>   r"   rA   )rr   rR   r   rc   rs   r<   )r
   ZstyleZdarkcmdZlightcmdr   r   r   r@   �   s    z
main.themec                 C   s�   t j�dd�r�t� }|�dd�}|dd � dkr@| j�d� d S d}| j�t�d	t	j
�t	j
�|�d
�g�� | j�t�dddt	j
�t	j
�|�d�g�� | j�t�d|t	j
�t	j
�|d
��g�� | j�t�d�d��� | j�d� t	�d� d S )NzWallpapper Injectoru�   Supported file types: 
.png 
•This script installs the selected wallpaper to your account,
but only for this monitor size. 
•May be required to run the script again when neccesary
•Only applies to your account after logon/logoff �/�\�����z.pngz#File format not valid. Must be .pngz"%appdata%\Microsoft\Windows\ThemesrZ   ZTranscodedWallpaperZRMDIRz/Sz/QZCachedFilesrV   ztaskkill /f /im explorer.exe� zApplying Wallpaperzexplorer.exe)r   rg   rh   r   �replacerR   r   rc   rd   r`   ra   re   ru   �split�system)r
   �filenameZwallpaper_locr   r   r   rB   �   s    (,*zmain.wallpaperc                 C   s   t j�dd�rt�d� d S )NzBrowser Themeu�   •Remove Https:// from URL
•Add : to the URL so it looks likes 'chrome://new-tab-page'
•Click bottom right edit icon
•Choose desired theme zhttps://chrome://new-tab-page)r   rg   rh   �
webbrowserZopen_new_tabr6   r   r   r   rC   �   s    zmain.chromeN)r   r   r   r   r(   r5   r;   rr   r<   r=   r}   r9   ro   rk   r@   rB   rC   r   r   r   r   r      s   4

r   )Ztkinterr   Ztkinter.messageboxr   r   Ztkinter.filedialogr   Zurllib.requestr�   rc   r`   r�   rx   ri   r'   Zos.pathr   r   r   r   r#   r   �mZmainloopr   r   r   r   �<module>   s   0	 P