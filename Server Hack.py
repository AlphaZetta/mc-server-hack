import time;

ip = None;
action = None;
b_action = None;
username = None;
b_unit = None;
m_action = None;
m_unit = None;
command = None;
cmd_exe = None;
icon = None;
title = None;
desc = None;
e_action = None;
amount = None;
giver = None;
receiver = None;

def restart():
    ip = None;
    action = None;
    b_action = None;
    username = None;
    b_unit = None;
    m_action = None;
    m_unit = None;
    command = None;
    cmd_exe = None;
    icon = None;
    title = None;
    desc = None;
    e_action = None;
    amount = None;
    giver = None;
    receiver = None;
    print("What action would you like to do?");
    print("Ban (ban), Kick (kick), Mute (mute), Warn (warn), Rank (rank), Custom Commands (cmd), Icon Changer (icon), Title Changer (title), Description Changer (desc), IP Changer (ip), Economy ($$$)");
    action = input();
    if action == 'ban':
        print("Ban (b) or tempban (t)?");
        b_action = input();
        if b_action == 'b':
            print("Username?");
            username = input();
            print("Banned " + username + " from " + ip);
            restart();
        elif b_action == 't':
            print("Username?");
            username = input();
            print("What unit of time?");
            print("Seconds (s), Minutes (m), Hours (h), Days (d), Weeks (w), Months (o), Years (y)");
            b_unit = input();
            if b_unit == 's':
                b_unit = 'seconds';
            elif b_unit == 'm':
                b_unit = 'minutes';
            elif b_unit == 'h':
                b_unit = 'hours';
            elif b_unit == 'd':
                b_unit = 'days';
            elif b_unit == 'w':
                b_unit = 'weeks';
            elif b_unit == 'o':
                b_unit = 'months';
            elif b_unit == 'y':
                b_unit = 'years';
            print("What number of " + b_unit + "?");
            b_time = input();
            print("Tempbanned " + username + " for " + b_time + " " + b_unit + " from " + ip);
            restart();
    elif action == 'kick':
        print("Username?");
        username = input();
        print("Kicked " + username + " from " + ip);
        restart();
    elif action == 'mute':
        print("Mute (m) or tempmute (t)?");
        m_action = input();
        if m_action == 'm':
            print("Username?");
            username = input();
            print("Muted " + username + " on " + ip);
            restart();
        elif m_action == 't':
            print("Username?");
            username = input();
            print("What unit of time?");
            print("Seconds (s), Minutes (m), Hours (h), Days (d), Weeks (w), Months (o), Years (y)");
            m_unit = input();
            if m_unit == 's':
                m_unit = 'seconds';
            elif m_unit == 'm':
                m_unit = 'minutes';
            elif m_unit == 'h':
                m_unit = 'hours';
            elif m_unit == 'd':
                m_unit = 'days';
            elif m_unit == 'w':
                m_unit = 'weeks';
            elif m_unit == 'o':
                m_unit = 'months';
            elif m_unit == 'y':
                m_unit = 'years';
            print("What number of " + m_unit + "?");
            m_time = input();
            print("Tempmuted " + username + " for " + m_time + " " + m_unit + " on " + ip);
            restart();
    elif action == 'warn':
        print('Username?');
        username = input();
        print('Warned ' + username);
        restart();
    elif action == 'rank':
        print('Username?');
        username = input();
        print("Rank?");
        print("Default (1), VIP (2), VIP+ (3), MVP (4), MVP+ (5), Overlord (6), Helper (7), Builer (8), Jr. Mod (9), Mod (10), Sr. Mod (11), Jr. Admin (12), Admin (13), Sr. Admin (14), Developer (15), Co-Owner (16), Owner (17)");
        rank = input();
        if rank == '1':
            rank = 'Default';
        elif rank == '2':
            rank = 'VIP';
        elif rank == '3':
            rank = 'VIP+';
        elif rank == '4':
            rank = 'MVP';
        elif rank == '5':
            rank = 'MVP+';
        elif rank == '6':
            rank = 'Overlord';
            
        elif rank == '7':
            rank = 'Helper';
        elif rank == '8':
            rank = 'Builder';
        elif rank == '9':
            rank = 'Jr. Mod';
        elif rank == '10':
            rank = 'Mod';
        elif rank == '11':
            rank = 'Sr. Mod';
        elif rank == '12':
            rank = 'Jr. Admin';
        elif rank == '13':
            rank = 'Admin';
        elif rank == '14':
            rank = 'Sr. Admin';
        elif rank == '15':
            rank = 'Developer';
        elif rank == '16':
            rank = 'Co-Owner';
        elif rank == '17':
            rank = 'Owner';
        print('Given ' + username + ' ' + rank + ' rank on ' + ip);
        restart();
    elif action == 'cmd':
        print("Name of this command?");
        command = input();
        print("What command are you assigning this custom command?");
        cmd_exe = input();
        print("Assigned command " + cmd_exe + " to custom command " + command + " on " + ip);
        restart();
    elif action == 'icon':
        print("Location/link of icon?");
        icon = input();
        print("Changed icon on " + ip + " to location " + icon);
        restart();
    elif action == 'title':
        print("What are you changing it to?");
        title = input();
        print("Changed title to " + title + " on " + ip);
        restart();
    elif action == 'desc':
        print("What are you changing it to?");
        desc = input();
        print("Changed title to " + desc + " on " + ip);
        restart();
    elif action == 'ip':
        print("What are you changing it to?");
        ip = input();
        print("Changed IP to " + ip);
        restart();
    elif action == '$$$':
        print("What action?");
        print("Add (a), remove (r), transfer (t)");
        e_action = input();
        if e_action == 'a':
            print("Username?");
            username = input();
            print("Amount?");
            amount = input();
            print("Given " + username + " " + amount + " coins");
            restart();
        elif e_action == 'r':
            print("Username?");
            username = input();
            print("Amount?");
            amount = input();
            print("Taken away " + amount + " coins from " + username);
            restart();
        elif e_action == 't':
            print("Giver?");
            giver = input();
            print("Receiver?");
            receiver = input();
            print("Amount?");
            amount = input();
            print("Transferred " + amount + " coins from " + giver + " to " + receiver);
            restart();

print("What is the server ip?");
ip = input();
print("Connecting to ip....");
time.sleep(3)
print("Injecting hacks...");
time.sleep(3);
print("Accessing database...");
time.sleep(3);
print("Accessed.");
print("What action would you like to do?");
print("Ban (ban), Kick (kick), Mute (mute), Warn (warn), Rank (rank), Custom Commands (cmd), Icon Changer (icon), Title Changer (title), Description Changer (desc), IP Changer (ip), Economy ($$$)");
action = input();
if action == 'ban':
    print("Ban (b) or tempban (t)?");
    b_action = input();
    if b_action == 'b':
        print("Username?");
        username = input();
        print("Banned " + username + " from " + ip);
        restart();
    elif b_action == 't':
        print("Username?");
        username = input();
        print("What unit of time?");
        print("Seconds (s), Minutes (m), Hours (h), Days (d), Weeks (w), Months (o), Years (y)");
        b_unit = input();
        if b_unit == 's':
            b_unit = 'seconds';
        elif b_unit == 'm':
            b_unit = 'minutes';
        elif b_unit == 'h':
            b_unit = 'hours';
        elif b_unit == 'd':
            b_unit = 'days';
        elif b_unit == 'w':
            b_unit = 'weeks';
        elif b_unit == 'o':
            b_unit = 'months';
        elif b_unit == 'y':
            b_unit = 'years';
        print("What number of " + b_unit + "?");
        b_time = input();
        print("Tempbanned " + username + " for " + b_time + " " + b_unit + " from " + ip);
        restart();
elif action == 'kick':
    print("Username?");
    username = input();
    print("Kicked " + username + " from " + ip);
    restart();
elif action == 'mute':
    print("Mute (m) or tempmute (t)?");
    m_action = input();
    if m_action == 'm':
        print("Username?");
        username = input();
        print("Muted " + username + " on " + ip);
        restart();
    elif m_action == 't':
        print("Username?");
        username = input();
        print("What unit of time?");
        print("Seconds (s), Minutes (m), Hours (h), Days (d), Weeks (w), Months (o), Years (y)");
        m_unit = input();
        if m_unit == 's':
            m_unit = 'seconds';
        elif m_unit == 'm':
            m_unit = 'minutes';
        elif m_unit == 'h':
            m_unit = 'hours';
        elif m_unit == 'd':
            m_unit = 'days';
        elif m_unit == 'w':
            m_unit = 'weeks';
        elif m_unit == 'o':
            m_unit = 'months';
        elif m_unit == 'y':
            m_unit = 'years';
        print("What number of " + m_unit + "?");
        m_time = input();
        print("Tempmuted " + username + " for " + m_time + " " + m_unit + " on " + ip);
        restart();
elif action == 'warn':
    print('Username?');
    username = input();
    print('Warned ' + username);
    restart();
elif action == 'rank':
    print('Username?');
    username = input();
    print("Rank?");
    print("Default (1), VIP (2), VIP+ (3), MVP (4), MVP+ (5), Overlord (6), Helper (7), Builer (8), Jr. Mod (9), Mod (10), Sr. Mod (11), Jr. Admin (12), Admin (13), Sr. Admin (14), Developer (15), Co-Owner (16), Owner (17)");
    rank = input();
    if rank == '1':
        rank = 'Default';
    elif rank == '2':
        rank = 'VIP';
    elif rank == '3':
        rank = 'VIP+';
    elif rank == '4':
        rank = 'MVP';
    elif rank == '5':
        rank = 'MVP+';
    elif rank == '6':
        rank = 'Overlord';
    elif rank == '7':
        rank = 'Helper';
    elif rank == '8':
        rank = 'Builder';
    elif rank == '9':
        rank = 'Jr. Mod';
    elif rank == '10':
        rank = 'Mod';
    elif rank == '11':
        rank = 'Sr. Mod';
    elif rank == '12':
        rank = 'Jr. Admin';
    elif rank == '13':
        rank = 'Admin';
    elif rank == '14':
        rank = 'Sr. Admin';
    elif rank == '15':
        rank = 'Developer';
    elif rank == '16':
        rank = 'Co-Owner';
    elif rank == '17':
        rank = 'Owner';
    print('Given ' + username + ' ' + rank + ' rank on ' + ip);
    restart();
elif action == 'cmd':
    print("Name of this command?");
    command = input();
    print("What command are you assigning this custom command?");
    cmd_exe = input();
    print("Assigned command " + cmd_exe + " to custom command " + command + " on " + ip);
    restart();
elif action == 'icon':
    print("Location/link of icon?");
    icon = input();
    print("Changed icon on " + ip + " to location " + icon);
    restart();
elif action == 'title':
    print("What are you changing it to?");
    title = input();
    print("Changed title to " + title + " on " + ip);
    restart();
elif action == 'desc':
    print("What are you changing it to?");
    desc = input();
    print("Changed title to " + desc + " on " + ip);
    restart();
elif action == 'ip':
    print("What are you changing it to?");
    ip = input();
    print("Changed IP to " + ip);
    restart();
elif action == '$$$':
    print("What action?");
    print("Add (a), remove (r), transfer (t)");
    e_action = input();
    if e_action == 'a':
        print("Username?");
        username = input();
        print("Amount?");
        amount = input();
        print("Given " + username + " " + amount + " coins");
        restart();
    elif e_action == 'r':
        print("Username?");
        username = input();
        print("Amount?");
        amount = input();
        print("Taken away " + amount + " coins from " + username);
        restart();
    elif e_action == 't':
        print("Giver?");
        giver = input();
        print("Receiver?");
        receiver = input();
        print("Amount?");
        amount = input();
        print("Transferred " + amount + " coins from " + giver + " to " + receiver);
        restart();
