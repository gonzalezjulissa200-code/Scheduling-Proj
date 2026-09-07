# Employee Shift Scheduler

A scheduling application for creating and managing employee shifts,
availability, coverage, and working-hour limits.

## Project Goals

The scheduler allows to manually create shifts, assign employees,
track employee hours, and scheduling conflicts.

## Structure

### Shift

Shift contains:

[x] Start time
[x] End time
[x] Duration
[x] Maximum employees per shift
[x] Assigned employees

Duration is calculated from start and end times and recalculated
whenever either time changes.

notes:
    base class is complete
    -need to work on being able to remove employees after theyve been assigned

### Employee

Employee contains:

- Name
- Availability
- Assigned shifts
- Total hours worked
- Maximum allowed hours
- Amount over maximum hours

Employee information can be edited.

## Shift Assignment

When assigning an employee to a shift, the scheduler displays possible
employees ranked by coverage.

Priority:

1. Full coverage with no warnings
2. Full coverage with warnings
3. Partial coverage
4. Employees exceeding their maximum hours

Warnings may include:

- Employee exceeds maximum hours
- Employee has an overlapping shift
- Employee cannot cover the entire shift

Coverage with a warning is preferred over less coverage.

For overlapping shifts, employees with smaller overlaps are ranked higher
than employees with larger overlaps.

## Scheduling Rules

- Shifts are created manually.
- Each shift has its own employee capacity.
- Employees can still be assigned when exceeding their maximum hours,
  but the scheduler displays a warning.
- Employee hours are calculated from their assigned shifts.
- Changes to shifts automatically update calculated employee hours.
