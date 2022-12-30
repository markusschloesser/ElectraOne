eqgain = controls.get(10)
eqq = controls.get(12)

function eqtype(valueObject, value)
    if value < 3 then
        eqgain:setVisible(true)
        eqq:setVisible(false)
    else
        eqgain:setVisible(false)
        eqq:setVisible(true)
    end
    if value == 0.0 then
        return("Low Shelf")
    elseif value == 1.0 then
        return("Bell")
    elseif value == 2.0 then
            return("High Shelf")
    elseif value == 3.0 then
            return("Low Pass")
    elseif value == 4.0 then
            return("Peak")
    else
        return("High Pass")
    end  
end
