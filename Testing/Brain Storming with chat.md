## Employee Shift Scheduling System

### 1. Business Hours

Business hours define when the business is open and closed.

They are mainly used for validation, since shifts will be created manually.

If a shift is created outside of business hours, the system can warn or prevent the user from saving it.

---

## 2. Shift

Each shift is created manually.

A shift should contain:

- Start time
    
- End time
    
- Maximum number of employees allowed
    

The shift duration should be calculated from the start and end times.

If the start or end time changes, the duration should automatically update.

A shift does not need to permanently store which employees are assigned to it. The scheduler can manage those relationships.

Example:

Shift  
Start: 8:00 AM  
End: 12:00 PM  
Duration: 4 hours  
Maximum Employees: 3

---

## 3. Employee

Each employee should be fully editable.

An employee should contain:

- Name
    
- Availability
    
- Assigned shifts
    
- Maximum hours allowed to work
    

Employees can have multiple availability periods on the same day.

Example:

Monday  
8:00 AM – 12:00 PM  
2:00 PM – 6:00 PM

The following values should be calculated instead of permanently stored:

- Total assigned hours
    
- Whether the employee is over their maximum hours
    
- How many hours they are over their maximum
    

If assigned shifts or maximum hours change, these values should automatically update.

---

## 4. Scheduler

The scheduler handles the relationship between employees and shifts.

Its responsibilities include:

- Managing employee assignments
    
- Comparing employee availability with shifts
    
- Calculating employee coverage
    
- Identifying warnings
    
- Ranking possible employees for a shift
    
- Checking shift capacity
    

The scheduler knows which employees are assigned to each shift.

---

## 5. Coverage Percentage

When selecting a shift, the scheduler compares that shift with each employee's availability.

Coverage is calculated as a percentage of the shift.

Example:

Shift: 10:00 AM – 4:00 PM  
Shift Length: 6 hours

Employee Availability:

8:00 AM – 12:00 PM  
2:00 PM – 6:00 PM

The employee can cover:

10:00 AM – 12:00 PM = 2 hours  
2:00 PM – 4:00 PM = 2 hours

Total Coverage: 4 hours

Coverage Percentage:

4 ÷ 6 = approximately 67%

Separate availability periods can be added together when calculating coverage.

---

## 6. Minimum Coverage Requirement

The system should have one global minimum coverage percentage.

Employees who do not meet the minimum are not shown as possible covers.

Employees who meet or exceed the minimum remain options even if they have warnings.

---

## 7. Warnings

Warnings provide useful information but do not automatically disqualify an employee.

Possible warnings include:

- Partial shift coverage
    
- Split availability during the shift
    
- Assignment would put the employee over their maximum hours
    
- Employee already has another assigned shift that overlaps
    

An employee can have multiple warnings for the same shift.

Warnings belong to the employee-and-shift comparison, not permanently to the employee.

For example, an employee may have no warnings for one shift but several warnings for another.

---

## 8. Possible Covers

When a shift is selected, the UI should display employees who meet the minimum coverage requirement.

Each possible cover can show:

- Employee name
    
- Coverage percentage
    
- Relevant warnings
    
- Current total hours
    
- Projected hours if assigned
    
- Whether they would exceed their maximum hours
    

Example:

Shift: 12:00 PM – 4:00 PM  
Duration: 4 hours  
Maximum Employees: 3

Possible Covers:

Employee A  
Coverage: 100%  
No warnings

Employee B  
Coverage: 100%  
Warning: Overlaps an existing shift by 30 minutes

Employee C  
Coverage: 100%  
Warning: Assignment would exceed maximum hours

Employee D  
Coverage: 85%  
Warning: Partial availability

---

## 9. Employee Ranking

Coverage percentage is always the most important ranking factor.

Higher coverage ranks above lower coverage, even if the higher-coverage employee has warnings.

For example:

100% coverage with a warning

ranks above:

80% coverage with no warnings

If coverage is tied, use the following priorities:

1. Prefer employees who stay within their maximum hours.
    
2. Prefer employees with less overlap with existing assigned shifts.
    
3. Longer overlaps should rank lower than shorter overlaps.
    

Warnings affect ranking between employees with similar coverage, but they do not automatically remove someone as an option.

---

## 10. Shift Capacity

Each shift has its own maximum employee capacity.

For example:

Morning Shift: Maximum 2 employees  
Evening Shift: Maximum 4 employees

The scheduler manages the actual assignments and can determine:

- How many employees are currently assigned
    
- How many spots remain
    
- Whether the shift is full
    

---

## 11. Editing

Both shifts and employees should be editable through the UI.

### Editable Shift Information

- Start time
    
- End time
    
- Maximum employee capacity
    

Duration recalculates automatically.

### Editable Employee Information

- Name
    
- Availability
    
- Maximum hours
    
- Assigned shifts
    

Calculated employee values update automatically after edits.

---

## 12. Main Design Principle

Stored information should be editable.

Calculated information should be derived from the stored information.

For example:

Stored:

- Shift start
    
- Shift end
    
- Shift capacity
    
- Employee availability
    
- Employee maximum hours
    
- Employee assigned shifts
    

Calculated:

- Shift duration
    
- Employee total hours
    
- Employee hours over maximum
    
- Coverage percentage
    
- Shift overlap
    
- Availability gaps
    
- Warnings
    
- Candidate ranking
    

---

## Overall Structure

**Shift**

Represents a block of working time.

Responsible for:

- Start time
    
- End time
    
- Duration
    
- Capacity
    

**Employee**

Represents an employee and their scheduling information.

Responsible for:

- Personal information
    
- Availability
    
- Assigned shifts
    
- Maximum hours
    
- Calculated workload information
    

**Scheduler**

Handles the relationship between shifts and employees.

Responsible for:

- Assignments
    
- Coverage calculations
    
- Warnings
    
- Candidate ranking
    
- Capacity checks