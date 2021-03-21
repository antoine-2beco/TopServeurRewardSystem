-- [[Format args for 3 args : cmdType, SteamID, money]] --
local function explodeArgs(args)
    if not istable(args) then return end

    if table.Count(args) != 7 then return end

    local formatedArgs = {}
   
    formatedArgs[1] = args[1]
    formatedArgs[2] = args[2]..args[3]..args[4]..args[5]..args[6]
    formatedArgs[3] = args[7]

    return formatedArgs
end

concommand.Add("mm", function(ply, cmd, args) 
    if IsValid(ply) && ply:IsPlayer() then

        if not ply:IsSuperAdmin() then return end
    end

    args = explodeArgs(args)
    if not istable(args) then return end

    args[3] = tonumber(args[3])
    if not args[1] or not args[2] or not isnumber(args[3]) then return end

    if args[1] ~= "addmoney" && args[1] ~= "setmoney" then return end

    local uid = util.SteamIDTo64(args[2]) 
    if not isstring(uid) then return end

    local target = player.GetBySteamID(args[2])

    local playerMoney = IsValid(target) and target:getDarkRPVar("money") or nil

    local rpname
    if not isnumber(moneyToSet) then
        rpname = sql.Query("SELECT rpname FROM darkrp_player WHERE uid = '"..uid.."'")[1].rpname if not isstring(rpname) then return end 
        playerMoney = tonumber(sql.Query("SELECT wallet FROM darkrp_player WHERE rpname = '"..rpname.."'")[1].wallet) 
    end
    if not isnumber(playerMoney) then return end 

    local moneyToSet = (args[1] == "addmoney" and playerMoney + args[3]) or (args[1] == "setmoney" and args[3])
    if not isnumber(moneyToSet) then return end

    if IsValid(target) then

        target:addMoney((moneyToSet - playerMoney))
    else

        sql.Query("UPDATE darkrp_player SET wallet = '"..moneyToSet.."' WHERE rpname = '"..rpname.."'")
    end
end)
